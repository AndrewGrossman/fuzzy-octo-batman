from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView, ModelFormMixin
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.db.models import Count
from braces.views import LoginRequiredMixin

# Attempt to handle path issues in environments that I do not have access to properly debug
try:
    from models import Position
    from forms import PositionForm, PositionConfirmDeleteForm
except ImportError:
    try:
        from .models import Position
        from .forms import PositionForm, PositionConfirmDeleteForm
    except ImportError:
        from resume.models import Position
        from resume.forms import PositionForm, PositionConfirmDeleteForm

import datetime
from django.utils import formats


class PositionObjectMixin(SingleObjectTemplateResponseMixin):
    model = Position

    def get_queryset(self):
        return super(PositionObjectMixin, self).get_queryset().filter(user=self.request.user.id)


class PositionFormMixin(PositionObjectMixin, ModelFormMixin):
    template_name = "resume/position_form.html"
    form_class = PositionForm
    success_url = '/resume/'
    is_update = False
    template_name_suffix = '_form'

    def get_initial(self):
        initial = super(PositionFormMixin, self).get_initial()
        initial.update({'user_id': self.request.user.id})
        return initial

    def get_form_kwargs(self):
        kwargs = super(PositionFormMixin, self).get_form_kwargs()

        if 'data' in kwargs:
            kwargs['data'] = kwargs['data'].dict()

            # Force the user to be the user logged in. Technically, this could cause weirdness if the user has multiple
            # windows, and submits something stale. Of course, CSRF is likely to blow that up anyway.
            kwargs['data'].update({'user': self.request.user.id})  # Force this to be the user that is logged in.

            def convert_month_year_field(value):
                try:
                    return datetime.datetime.strptime(value, "%B %Y").strftime(formats.get_format('DATE_INPUT_FORMATS')[0])
                except ValueError:
                    return value  # Let the field validator handle it

            # Really, this should be cleaned on the field or the form, but it was easier to just do it here.
            if 'employment_start_date' in kwargs['data'] and kwargs['data']['employment_start_date'].strip():
                kwargs['data']['employment_start_date'] = \
                    convert_month_year_field(kwargs['data']['employment_start_date'])

            if 'employment_end_date' in kwargs['data'] and kwargs['data']['employment_end_date'].strip():
                kwargs['data']['employment_end_date'] = \
                    convert_month_year_field(kwargs['data']['employment_end_date'])

        kwargs['is_update'] = self.is_update

        return kwargs


class PositionCreateView(LoginRequiredMixin, PositionFormMixin, CreateView):
    is_update = False


class PositionUpdateView(LoginRequiredMixin, PositionFormMixin, UpdateView):
    is_update = True


class PositionDeleteView(PositionObjectMixin, DeleteView):
    success_url = '/resume/'

    def get_context_data(self, **kwargs):
        context = super(PositionDeleteView, self).get_context_data(**kwargs)
        context['form'] = PositionConfirmDeleteForm()
        return context


# Honestly, I've got tons more practice with function based views. There's a great piece out there on why
# the CBV system is inferior.
def positions_list(request, template="resume/position_list.html", *args, **kwargs):
    # Use annotate to order the queryset as needed
    positions = Position.objects.filter(user_id=request.user.id). \
        annotate(null_employment_end_date=Count('employment_end_date')). \
        order_by('null_employment_end_date', '-employment_end_date', '-employment_start_date')
    return render(request, template, locals())

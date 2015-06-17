from django.forms import ModelForm, Form
from models import Position
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Div, HTML
from django.forms.widgets import HiddenInput
from django.forms import ValidationError
from django.utils.translation import ugettext as _
from datetime import date

from datetimewidget.widgets import DateWidget

# datetimewidget's widgets aren't particularly good at custom formats. Handle that partly here.
class MonthYearDateWidget(DateWidget):
    def __init__(self, *args, **kwargs):
        super(MonthYearDateWidget, self).__init__(*args, **kwargs)
        self.format = "%B %Y"


class PositionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        is_update = kwargs.pop('is_update', False)

        if not is_update:
            submit_button_text = _('Add Position')
        else:
            submit_button_text = _('Update Position')

        super(PositionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-positionForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 position-label'
        self.helper.field_class = 'col-md-8 position-field'
        self.helper.layout = Layout(
            'user',
            'title', 'company', 'location',
            Div(Field('employment_start_date', css_class='col-md-4'),
                Field('employment_end_date', css_class='col-md-4')),
            Div(Submit('submit', submit_button_text, ),
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url "resume:position-list" %}">Cancel</a>"""),
                css_class='col-md-offset-2 col-md-4',
                ),
        )

    def clean(self):
        cleaned_data = super(PositionForm, self).clean()
        employment_start_date = cleaned_data.get("employment_start_date")
        employment_end_date = cleaned_data.get("employment_end_date")

        if employment_end_date and employment_start_date > employment_end_date:
            raise ValidationError(
                "Check your dates. Traditionally, positions end after they have begun."
            )

    class Meta:
        model = Position
        exclude = ('created_timestamp', 'modified_timestamp')
        widgets = {
            # Use localization and bootstrap3
            'employment_start_date': MonthYearDateWidget(attrs={'id': "employment_start_date_id"},
                                                         bootstrap_version=3,
                                                         usel10n=False,
                                                         # Unfortunately, l10n breaks custom date formats
                                                         options={'minView': 3, 'startView': 4, 'format': "MM yyyy",
                                                                  'endDate': date.today().strftime("%B %Y")}),
            'employment_end_date': MonthYearDateWidget(attrs={'id': "employment_end_date_id"}, bootstrap_version=3,
                                                       usel10n=False,  # Unfortunately, l10n breaks custom date formats
                                                       options={'minView': 3, 'startView': 4, 'format': "MM yyyy",
                                                                'endDate': date.today().strftime("%B %Y")}),
            'user': HiddenInput(),
        }


class PositionConfirmDeleteForm(Form):
    def __init__(self, *args, **kwargs):
        super(PositionConfirmDeleteForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-positionConfirmDeleteForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-2 position-label'
        self.helper.field_class = 'col-md-8 position-field'
        self.helper.layout = Layout(
            Div(Submit('submit', _('Confirm Delete'), ),
                HTML("""<a role="button" class="btn btn-default"
                        href="{% url "resume:position-list" %}">Cancel</a>"""),
                css_class='col-md-offset-2 col-md-4 text-center',
                ),
        )

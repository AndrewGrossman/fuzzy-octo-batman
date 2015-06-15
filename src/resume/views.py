from django.shortcuts import render
from django.views import generic
from forms import PositionForm

class ResumePage(generic.TemplateView):
    template_name = "resume/resume.html"
    
    def get_context_data(self, **kwargs):
        context = super(ResumePage, self).get_context_data(**kwargs)
        context['form'] = PositionForm()
        return context
    
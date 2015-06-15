from django.forms import ModelForm, CharField
from models import Position
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.utils.translation import ugettext as _
from datetime import date

from datetimewidget.widgets import DateWidget

class PositionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-positionForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_position'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
            'title', 'company', 'location', 'employment_start_date', 'employment_end_date', 
            Submit('submit', _('Add Position')),)
        
    class Meta:
        model = Position
        fields = ['title', 'company', 'location', 'employment_start_date', 'employment_end_date']        
        widgets = {
            #Use localization and bootstrap 3
            'employment_start_date': DateWidget(attrs={'id':"employment_start_date_id"}, usel10n = True, bootstrap_version=3, 
                                                options={'minView': 3, 'startView': 4, 'format': "yyyy"}),
                                                # An endDate option of date.today().strftime("%d/%m/%Y") just broke things on the frontend
            'employment_end_date': DateWidget(attrs={'id':"employment_end_date_id"}, usel10n = True, bootstrap_version=3, 
                                              options={'minView': 3, 'startView': 4})
        }
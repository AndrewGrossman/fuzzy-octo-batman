from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _

class Position(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256, verbose_name=_('Position held'))
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    employment_start_date = models.DateField(verbose_name=_('Started on'))
    employment_end_date = models.DateField(null=True, blank=True, verbose_name=_('Ended on'))
    
    class Meta:
        ordering = ["user_id", "-employment_end_date", "-employment_start_date", ]
        index_together = [ ["user_id", "employment_end_date", "employment_start_date"],
                         ]

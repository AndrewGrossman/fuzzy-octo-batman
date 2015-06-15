from django.db import models
from django.conf import settings

class Position(models.Model):
    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_timestamp = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    company = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    employment_start_date = models.DateField(db_index=True)
    employment_end_date = models.DateField(null=True, blank=True)
	

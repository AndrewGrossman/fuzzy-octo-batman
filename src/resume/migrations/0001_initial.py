# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('modified_timestamp', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256)),
                ('company', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('employment_start_date', models.DateField(db_index=True)),
                ('employment_end_date', models.DateField(null=True, blank=True)),
                ('user_id', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20150615_0053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['user_id', '-employment_end_date', '-employment_start_date']},
        ),
    ]

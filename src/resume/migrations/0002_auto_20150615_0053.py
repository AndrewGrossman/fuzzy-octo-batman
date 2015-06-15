# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['-employment_end_date', '-employment_start_date']},
        ),
        migrations.AlterField(
            model_name='position',
            name='employment_start_date',
            field=models.DateField(),
        ),
        migrations.AlterIndexTogether(
            name='position',
            index_together=set([('user_id', 'employment_end_date', 'employment_start_date')]),
        ),
    ]

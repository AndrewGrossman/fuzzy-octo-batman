# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20150615_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['user', '-employment_end_date', '-employment_start_date']},
        ),
        migrations.RenameField(
            model_name='position',
            old_name='user_id',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='position',
            name='employment_end_date',
            field=models.DateField(null=True, verbose_name='Ended on', blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='employment_start_date',
            field=models.DateField(verbose_name='Started on'),
        ),
        migrations.AlterField(
            model_name='position',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Position held'),
        ),
        migrations.AlterIndexTogether(
            name='position',
            index_together=set([('user', 'employment_end_date', 'employment_start_date')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_profile_profile_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Career',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AddField(
            model_name='profile',
            name='Sex_Type',
            field=models.CharField(default='D', max_length=1, choices=[('M', 'Male'), ('F', 'Female'), ('D', 'default')]),
        ),
    ]

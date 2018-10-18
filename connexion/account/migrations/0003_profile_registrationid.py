# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_profile_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='RegistrationID',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]

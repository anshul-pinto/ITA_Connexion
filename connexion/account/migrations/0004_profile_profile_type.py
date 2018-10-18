# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_profile_registrationid'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Profile_type',
            field=models.CharField(default='ST', choices=[('ST', 'Student'), ('FC', 'Faculty'), ('AL', 'Alumni')], max_length=2),
        ),
    ]

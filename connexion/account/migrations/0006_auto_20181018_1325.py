# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20181018_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Exclusive_Club',
            field=models.CharField(default='N', choices=[('R', 'Rotaract'), ('I', 'IEEE'), ('A', 'ACM'), ('E', 'IE'), ('N', 'None')], max_length=1),
        ),
        migrations.AddField(
            model_name='profile',
            name='Other_Clubs',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]

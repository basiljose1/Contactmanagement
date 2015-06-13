# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='people',
            field=models.ManyToManyField(null=True, to='contacts.Name', verbose_name='first_name', blank=True),
        ),
        migrations.AlterField(
            model_name='name',
            name='gender',
            field=models.CharField(max_length=200, default='male', verbose_name='gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20150612_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='people',
            field=models.ManyToManyField(blank=True, to='contacts.Name', null=True, verbose_name='Names'),
        ),
    ]

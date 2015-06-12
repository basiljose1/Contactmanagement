# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('from_date', models.DateTimeField(verbose_name='From date')),
                ('to_date', models.DateTimeField(verbose_name='To date')),
                ('list_size', models.IntegerField(default=1)),
                ('total_email', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('group_code', models.CharField(max_length=16, unique=True)),
                ('group_name', models.CharField(max_length=200)),
                ('Group_des', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=200)),
                ('group_code', models.ForeignKey(to='contacts.Group')),
            ],
        ),
        migrations.AddField(
            model_name='contract',
            name='contract',
            field=models.ForeignKey(to='contacts.Name'),
        ),
    ]

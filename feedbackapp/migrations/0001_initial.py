# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-12-20 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBackDatamodels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('date', models.DateTimeField(max_length=100)),
                ('Feedback', models.CharField(max_length=100)),
            ],
        ),
    ]
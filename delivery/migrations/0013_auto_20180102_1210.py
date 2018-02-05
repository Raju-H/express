# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-02 06:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0012_auto_20171231_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='toppings',
        ),
        migrations.RemoveField(
            model_name='tripcost',
            name='trip_number',
        ),
        migrations.RemoveField(
            model_name='triplist',
            name='trip_number',
        ),
        migrations.RemoveField(
            model_name='tripnumber',
            name='car_no',
        ),
        migrations.RemoveField(
            model_name='tripnumber',
            name='driver_name',
        ),
        migrations.DeleteModel(
            name='CarList',
        ),
        migrations.DeleteModel(
            name='DriverName',
        ),
        migrations.DeleteModel(
            name='Pizza',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
        migrations.DeleteModel(
            name='TripCost',
        ),
        migrations.DeleteModel(
            name='TripList',
        ),
        migrations.DeleteModel(
            name='TripNumber',
        ),
    ]
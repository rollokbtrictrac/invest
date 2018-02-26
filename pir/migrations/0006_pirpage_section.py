# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-15 14:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pir', '0005_auto_20180214_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='pirpage',
            name='section',
            field=models.CharField(choices=[('0', 'Front Page'), ('1', 'Sector Overview'), ('2', 'Killer Facts'), ('3', 'Macro Context Between Countries'), ('4', 'UK Market Overview'), ('5', 'UK Business Info'), ('6', 'UK Geographic Overview'), ('7', 'Talent & Education'), ('8', 'Sector Initiatives'), ('9', 'R&D and Innovation'), ('10', 'R&D Innovation Case Study - Written'), ('11', "Who's Here?"), ('12', 'Video Case Study'), ('13', 'Services offered by DIT'), ('14', 'Call to Action'), ('15', 'Testimonials')], default=1, max_length=64),
            preserve_default=False,
        ),
    ]
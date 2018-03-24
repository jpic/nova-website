# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-11 23:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novaAPI', '0002_auto_20180311_1921'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Develop',
            new_name='AboutUs',
        ),
        migrations.RenameModel(
            old_name='SolutionsProduction',
            new_name='CrossIndustry',
        ),
        migrations.RenameModel(
            old_name='Consultancy',
            new_name='Industry',
        ),
        migrations.RenameModel(
            old_name='Publishing',
            new_name='LearningLab',
        ),
        migrations.RenameModel(
            old_name='PartnershipProduction',
            new_name='Network',
        ),
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'About Us', 'verbose_name_plural': 'About Us'},
        ),
        migrations.AlterModelOptions(
            name='blogpost',
            options={'verbose_name': 'Blog Post', 'verbose_name_plural': 'Lab Live'},
        ),
        migrations.AlterModelOptions(
            name='businessproposition',
            options={'verbose_name': 'Business Proposition', 'verbose_name_plural': 'Business Propositions'},
        ),
        migrations.AlterModelOptions(
            name='network',
            options={'verbose_name': 'Network', 'verbose_name_plural': 'Network'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AlterModelOptions(
            name='publication',
            options={'verbose_name': 'Publication', 'verbose_name_plural': 'Publications'},
        ),
    ]

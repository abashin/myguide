# Generated by Django 3.0.8 on 2022-11-23 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20221123_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='guide_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='имя гида'),
        ),
    ]

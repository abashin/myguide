# Generated by Django 3.0.8 on 2023-03-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_region_svg'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='svg_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='svg'),
        ),
    ]

# Generated by Django 3.0.8 on 2023-03-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_region_svg_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='transit_link',
            field=models.CharField(default='', max_length=30, verbose_name='имя для ссылки'),
        ),
    ]

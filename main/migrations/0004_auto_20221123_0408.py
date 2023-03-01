# Generated by Django 3.0.8 on 2022-11-23 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20221123_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='district',
            name='guide_description',
            field=models.TextField(blank=True, verbose_name='описание экскурсовода'),
        ),
        migrations.AlterField(
            model_name='request',
            name='resume',
            field=models.BooleanField(default=False, verbose_name='заявка-резюме'),
        ),
    ]

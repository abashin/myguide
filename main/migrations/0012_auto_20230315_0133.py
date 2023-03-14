# Generated by Django 3.0.8 on 2023-03-14 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20230315_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='caption10',
            field=models.CharField(blank=True, max_length=50, verbose_name='подпись10'),
        ),
        migrations.AddField(
            model_name='district',
            name='caption8',
            field=models.CharField(blank=True, max_length=50, verbose_name='подпись8'),
        ),
        migrations.AddField(
            model_name='district',
            name='caption9',
            field=models.CharField(blank=True, max_length=50, verbose_name='подпись9'),
        ),
        migrations.AddField(
            model_name='district',
            name='image10',
            field=models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка10'),
        ),
        migrations.AddField(
            model_name='district',
            name='image8',
            field=models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка8'),
        ),
        migrations.AddField(
            model_name='district',
            name='image9',
            field=models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка9'),
        ),
        migrations.AddField(
            model_name='district',
            name='text10',
            field=models.TextField(blank=True, verbose_name='текст10'),
        ),
        migrations.AddField(
            model_name='district',
            name='text8',
            field=models.TextField(blank=True, verbose_name='текст8'),
        ),
        migrations.AddField(
            model_name='district',
            name='text9',
            field=models.TextField(blank=True, verbose_name='текст9'),
        ),
        migrations.AddField(
            model_name='district',
            name='title10',
            field=models.CharField(blank=True, max_length=50, verbose_name='заголовок10'),
        ),
        migrations.AddField(
            model_name='district',
            name='title8',
            field=models.CharField(blank=True, max_length=50, verbose_name='заголовок8'),
        ),
        migrations.AddField(
            model_name='district',
            name='title9',
            field=models.CharField(blank=True, max_length=50, verbose_name='заголовок9'),
        ),
    ]

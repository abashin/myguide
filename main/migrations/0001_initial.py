# Generated by Django 3.0.8 on 2022-11-23 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='название')),
                ('map', models.ImageField(blank=True, upload_to='maps/', verbose_name='карта округа')),
                ('description', models.TextField(verbose_name='описание')),
            ],
            options={
                'verbose_name': 'Округ',
                'verbose_name_plural': 'Округи',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, verbose_name='имя')),
                ('description', models.TextField(verbose_name='способ связи')),
                ('resume', models.BooleanField(default=True, verbose_name='заявка-резюме')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guide_name', models.CharField(max_length=30, verbose_name='имя гида')),
                ('guide_avatar', models.ImageField(blank=True, upload_to='avatars/', verbose_name='аватарка экскурсовода')),
                ('guide_description', models.TextField(verbose_name='описание экскурсовода')),
                ('map', models.ImageField(blank=True, upload_to='maps/', verbose_name='карта района')),
                ('name', models.CharField(max_length=30, verbose_name='название')),
                ('image1', models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка1')),
                ('image2', models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка2')),
                ('image3', models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка3')),
                ('image4', models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка4')),
                ('image5', models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка5')),
                ('image6', models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка6')),
                ('image7', models.ImageField(blank=True, upload_to='district_images/', verbose_name='картинка7')),
                ('text1', models.TextField(blank=True, verbose_name='текст1')),
                ('text2', models.TextField(blank=True, verbose_name='текст2')),
                ('text3', models.TextField(blank=True, verbose_name='текст3')),
                ('text4', models.TextField(blank=True, verbose_name='текст4')),
                ('text5', models.TextField(blank=True, verbose_name='текст5')),
                ('text6', models.TextField(blank=True, verbose_name='текст6')),
                ('text7', models.TextField(blank=True, verbose_name='текст7')),
                ('region', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.Region')),
            ],
            options={
                'verbose_name': 'Район',
                'verbose_name_plural': 'Районы',
            },
        ),
    ]

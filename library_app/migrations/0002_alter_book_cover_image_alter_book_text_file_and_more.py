# Generated by Django 5.1.4 on 2024-12-23 20:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='covers/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='text_file',
            field=models.FileField(blank=True, null=True, upload_to='texts/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)]),
        ),
    ]

# Generated by Django 4.1 on 2022-08-24 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_gallery_gallery_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='gallery_description',
        ),
    ]

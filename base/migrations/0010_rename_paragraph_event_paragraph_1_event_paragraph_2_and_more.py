# Generated by Django 4.1 on 2022-08-24 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_remove_gallery_gallery_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='paragraph',
            new_name='paragraph_1',
        ),
        migrations.AddField(
            model_name='event',
            name='paragraph_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='paragraph_3',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

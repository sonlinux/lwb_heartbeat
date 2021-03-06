# Generated by Django 2.0.5 on 2018-05-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='date_modified',
            new_name='date_photo_taken',
        ),
        migrations.AddField(
            model_name='photo',
            name='image_title',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='location',
            field=models.CharField(blank=True, default='none', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, max_length=4000, null=True),
        ),
    ]

# Generated by Django 2.0.5 on 2018-05-22 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='child',
        ),
    ]
# Generated by Django 2.0.5 on 2018-05-24 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0004_auto_20180524_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalupdate',
            name='child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.Child'),
        ),
        migrations.AlterField(
            model_name='medicalupdate',
            name='child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.Child'),
        ),
    ]

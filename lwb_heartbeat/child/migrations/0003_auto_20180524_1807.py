# Generated by Django 2.0.5 on 2018-05-24 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('child', '0002_auto_20180524_0205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='growthdata',
            old_name='height',
            new_name='height_cm',
        ),
        migrations.RenameField(
            model_name='growthdata',
            old_name='weight',
            new_name='weight_kg',
        ),
        migrations.AlterField(
            model_name='growthdata',
            name='child',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='child.Child'),
        ),
    ]

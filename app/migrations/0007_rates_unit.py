# Generated by Django 3.2.9 on 2022-02-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_rates_type_of_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='rates',
            name='Unit',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

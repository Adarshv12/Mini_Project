# Generated by Django 3.2.9 on 2022-06-22 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_tbl_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_projects',
            name='lat',
            field=models.FloatField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tbl_projects',
            name='lon',
            field=models.FloatField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.9 on 2022-01-18 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company_details',
            name='D_id',
        ),
        migrations.RemoveField(
            model_name='contractor_details',
            name='D_id',
        ),
        migrations.RemoveField(
            model_name='details',
            name='type_id',
        ),
        migrations.RemoveField(
            model_name='worker_details',
            name='D_id',
        ),
        migrations.RemoveField(
            model_name='worker_details',
            name='W_name',
        ),
    ]
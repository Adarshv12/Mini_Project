# Generated by Django 3.2.9 on 2022-06-25 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20220625_1038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tbl_contractor_invite',
            name='cinvite_id',
        ),
    ]

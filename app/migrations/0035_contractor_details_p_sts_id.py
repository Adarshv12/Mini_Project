# Generated by Django 3.2.9 on 2022-06-23 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_tbl_contractor_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractor_details',
            name='p_sts_id',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.2.9 on 2022-07-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_alter_tbl_payments_bamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_payments',
            name='payment_id',
            field=models.CharField(max_length=50),
        ),
    ]

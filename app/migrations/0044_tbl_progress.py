# Generated by Django 3.2.9 on 2022-07-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_alter_tbl_payments_payment_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_progress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=10)),
                ('progress', models.IntegerField()),
                ('label', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tbl_progress',
            },
        ),
    ]

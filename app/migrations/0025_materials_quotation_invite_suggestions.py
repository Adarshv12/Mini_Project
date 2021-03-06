# Generated by Django 3.2.9 on 2022-06-19 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_work_invite'),
    ]

    operations = [
        migrations.CreateModel(
            name='materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('M_name', models.CharField(max_length=40)),
                ('Type', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'materials',
            },
        ),
        migrations.CreateModel(
            name='quotation_invite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=30)),
                ('Loc', models.CharField(max_length=30)),
                ('Contrator_id', models.CharField(max_length=20)),
                ('Plan_img', models.CharField(max_length=100)),
                ('Sugg_id', models.CharField(max_length=10)),
                ('Customer_id', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'quotation_invite',
            },
        ),
        migrations.CreateModel(
            name='suggestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=30)),
                ('suggestion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'suggestions',
            },
        ),
    ]

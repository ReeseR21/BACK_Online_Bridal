# Generated by Django 3.2.8 on 2021-10-12 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebridal', '0016_alter_onlinebridal_participation'),
    ]

    operations = [
        migrations.CreateModel(
            name='BridalParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.IntegerField(default=True)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='GuestList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=25)),
                ('state', models.CharField(max_length=25)),
                ('zip_code', models.IntegerField(default=True)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]

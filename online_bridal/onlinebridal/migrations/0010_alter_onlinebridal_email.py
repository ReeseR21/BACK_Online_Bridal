# Generated by Django 3.2.8 on 2021-10-11 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebridal', '0009_alter_onlinebridal_participation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinebridal',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-08 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebridal', '0005_alter_onlinebridal_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='onlinebridal',
            name='email',
            field=models.CharField(default=True, max_length=200),
        ),
    ]

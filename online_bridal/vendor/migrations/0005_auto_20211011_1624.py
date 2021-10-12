# Generated by Django 3.2.8 on 2021-10-11 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0004_rename_vendors_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='description',
            field=models.TextField(blank=True, max_length=250),
        ),
        migrations.AddField(
            model_name='vendor',
            name='price_range',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='business_email',
            field=models.CharField(default=True, max_length=75),
        ),
    ]
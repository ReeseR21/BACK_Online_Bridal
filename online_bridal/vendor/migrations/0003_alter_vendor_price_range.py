# Generated by Django 3.2.8 on 2021-10-14 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_auto_20211013_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='price_range',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]

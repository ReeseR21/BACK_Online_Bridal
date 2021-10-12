# Generated by Django 3.2.8 on 2021-10-12 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinebridal', '0015_alter_onlinebridal_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onlinebridal',
            name='participation',
            field=models.CharField(choices=[('BR', 'Bride'), ('GR', 'Groom'), ('GU', 'Guest'), ('MH', 'Maid Of Honor'), ('BRM', 'Bridesmaid'), ('BM', 'Bestman'), ('GM', 'Groomsmen'), ('FG', 'Flower Girl'), ('RB', 'Ring Bearer')], max_length=15),
        ),
    ]
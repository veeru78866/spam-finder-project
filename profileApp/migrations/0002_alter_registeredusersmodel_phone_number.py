# Generated by Django 4.1.7 on 2023-03-15 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeredusersmodel',
            name='phone_number',
            field=models.IntegerField(max_length=12),
        ),
    ]

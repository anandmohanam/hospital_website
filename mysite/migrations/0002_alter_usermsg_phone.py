# Generated by Django 5.0.4 on 2024-05-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermsg',
            name='phone',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-22 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_alter_usermsg_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='indexmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics')),
            ],
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-26 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_user_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
# Generated by Django 4.1.2 on 2022-12-15 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='slug',
        ),
    ]

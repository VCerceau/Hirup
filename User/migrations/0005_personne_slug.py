# Generated by Django 4.1.4 on 2022-12-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_remove_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='personne',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
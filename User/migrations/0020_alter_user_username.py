# Generated by Django 4.1.2 on 2022-11-26 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0019_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
# Generated by Django 4.1.2 on 2022-11-22 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profilpic',
            field=models.CharField(max_length=512, null=True),
        ),
    ]

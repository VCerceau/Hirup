# Generated by Django 4.1.2 on 2022-11-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0024_alter_user_profilpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilpic',
            field=models.ImageField(default='user/pp/default.webp', null=True, upload_to='user/pp'),
        ),
    ]

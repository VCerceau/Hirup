# Generated by Django 4.1.2 on 2022-11-26 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_alter_user_profilpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilpic',
            field=models.ImageField(blank=True, default='user/pp/default.png', null=True, upload_to='user/pp'),
        ),
    ]
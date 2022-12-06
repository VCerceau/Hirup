# Generated by Django 4.1.2 on 2022-12-06 12:46

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0025_alter_user_profilpic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilpic',
            field=django_resized.forms.ResizedImageField(crop=None, default='user/pp/default.webp', force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[200, 200], upload_to='user/pp'),
        ),
    ]
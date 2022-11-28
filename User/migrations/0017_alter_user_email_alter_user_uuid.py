# Generated by Django 4.1.2 on 2022-11-26 13:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
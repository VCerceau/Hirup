# Generated by Django 4.1.2 on 2022-12-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Presentation', '0004_alter_cv_ord_comp_alter_cv_ord_form_alter_cv_ord_xp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competence',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]

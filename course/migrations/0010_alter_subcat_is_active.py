# Generated by Django 4.2.1 on 2023-06-06 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcat',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]

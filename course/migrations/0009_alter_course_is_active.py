# Generated by Django 4.2.1 on 2023-06-03 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_alter_course_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
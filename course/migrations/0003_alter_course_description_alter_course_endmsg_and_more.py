# Generated by Django 4.2.1 on 2023-05-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_session_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='course',
            name='endmsg',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='course',
            name='welcomemsg',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='session',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-15 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='discription',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

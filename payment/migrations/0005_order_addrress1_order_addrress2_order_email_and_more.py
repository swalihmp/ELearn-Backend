# Generated by Django 4.2.1 on 2023-06-09 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='addrress1',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='addrress2',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='firtname',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='lastname',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
    ]

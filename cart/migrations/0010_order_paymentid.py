# Generated by Django 2.2 on 2022-05-06 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_order_customerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paymentId',
            field=models.IntegerField(default=1),
        ),
    ]

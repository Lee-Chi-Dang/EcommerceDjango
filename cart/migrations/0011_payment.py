# Generated by Django 2.2 on 2022-05-06 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_order_paymentid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Paypal'), (2, 'Cast')], default=2)),
            ],
        ),
    ]
# Generated by Django 2.2 on 2022-03-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilephone', '0004_auto_20220321_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilephonea',
            name='chip',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mobilephonea',
            name='os',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='mobilephonea',
            name='ram',
            field=models.CharField(default='', max_length=50),
        ),
    ]

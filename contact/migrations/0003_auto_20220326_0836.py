# Generated by Django 2.2 on 2022-03-26 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20220326_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactabc',
            name='comment',
            field=models.TextField(default='', max_length=5),
        ),
    ]

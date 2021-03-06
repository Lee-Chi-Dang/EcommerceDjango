# Generated by Django 2.2 on 2022-03-21 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mobilephone', '0005_auto_20220321_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhoneItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(max_length=50)),
                ('discount', models.CharField(max_length=50)),
                ('inventory', models.IntegerField(default=0)),
                ('mobilePhone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mobilephone.MobilePhoneA')),
            ],
        ),
    ]

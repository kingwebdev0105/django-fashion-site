# Generated by Django 2.2.7 on 2021-04-24 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kowiapp', '0007_auto_20210424_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custinfo',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]

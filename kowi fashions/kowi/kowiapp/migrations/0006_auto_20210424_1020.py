# Generated by Django 2.2.7 on 2021-04-24 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kowiapp', '0005_auto_20210424_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custinfo',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='custinfo',
            name='lng',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]

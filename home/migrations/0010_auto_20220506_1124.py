# Generated by Django 3.2.13 on 2022-05-06 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20220506_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inoutmaterial',
            name='tglIn',
            field=models.DateField(blank=True, verbose_name='Tanggal Masuk'),
        ),
        migrations.AlterField(
            model_name='inoutmaterial',
            name='tglOut',
            field=models.DateField(blank=True, verbose_name='Tanggal Keluar'),
        ),
    ]

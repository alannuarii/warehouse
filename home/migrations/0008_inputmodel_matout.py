# Generated by Django 3.2.13 on 2022-05-06 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20220506_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputmodel',
            name='matOut',
            field=models.IntegerField(default=0, verbose_name='Material Keluar'),
        ),
    ]

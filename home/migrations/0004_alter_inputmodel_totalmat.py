# Generated by Django 3.2.13 on 2022-05-02 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220502_2156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputmodel',
            name='totalMat',
            field=models.IntegerField(verbose_name='Total Material'),
        ),
    ]
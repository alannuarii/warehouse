# Generated by Django 3.2.13 on 2022-05-03 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_inputmodel_totalmat'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOutMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tglIn', models.DateField(verbose_name='Tanggal Masuk')),
                ('tglOut', models.DateField(verbose_name='Tanggal Keluar')),
                ('nmrMat', models.CharField(max_length=200, verbose_name='Nomor Material')),
                ('descMat', models.CharField(max_length=200, verbose_name='Deskripsi Material')),
                ('jmlMat', models.IntegerField(verbose_name='Jumlah Material')),
                ('satuan', models.CharField(max_length=200, verbose_name='Satuan')),
                ('hargaSat', models.IntegerField(verbose_name='Harga Satuan')),
                ('totalMat', models.IntegerField(verbose_name='Total Material')),
            ],
        ),
    ]
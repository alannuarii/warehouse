# Generated by Django 3.2.13 on 2022-05-02 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_inputmodel_imgmat'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputmodel',
            name='totalMat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='descMat',
            field=models.CharField(max_length=200, verbose_name='Deskripsi Material'),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='hargaSat',
            field=models.IntegerField(verbose_name='Harga Satuan'),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='imgMat',
            field=models.ImageField(upload_to='static/uploads/img', verbose_name='Foto Material'),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='jmlMat',
            field=models.IntegerField(verbose_name='Jumlah Material'),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='nmrMat',
            field=models.CharField(max_length=200, verbose_name='Nomor Material'),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='satuan',
            field=models.CharField(max_length=200, verbose_name='Satuan'),
        ),
        migrations.AlterField(
            model_name='inputmodel',
            name='tglMasuk',
            field=models.DateField(verbose_name='Tanggal Masuk'),
        ),
    ]

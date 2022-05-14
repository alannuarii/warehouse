from pyexpat import model
from django.db import models

# Create your models here.
class InputModel(models.Model):
    tglMasuk = models.DateField('Tanggal Masuk',blank=True)
    nmrMat = models.CharField('Nomor Material',max_length=200)
    descMat = models.CharField('Deskripsi Material',max_length=200)
    jmlMat = models.IntegerField('Jumlah Material')
    matIn = models.IntegerField('Material Masuk',default=0)
    matOut = models.IntegerField('Material Keluar',default=0)
    satuan = models.CharField('Satuan',max_length=200)
    hargaSat = models.IntegerField('Harga Satuan')
    random = models.IntegerField('Random') 
    stock = models.IntegerField('Stock')
    totalMat = models.IntegerField('Total Material')
    imgMat = models.ImageField('Foto Material',upload_to='static/uploads/img')
    
    class Meta:
        unique_together = ['nmrMat']

    @property
    def stockMat(self):
        stockIn = int(self.jmlMat) + int(self.matIn) - int(self.matOut)
        return stockIn

    @property
    def totMat(self):
        total = int(self.stock) * int(self.hargaSat)
        return total

    def save(self, *args, **kwargs):
        self.stock = self.stockMat
        self.totalMat = self.totMat
        super(InputModel, self).save(*args, **kwargs)

    

    # def save(self, *args, **kwargs):
    #     self.stock = self.stockMat
    #     super(InputModel, self).save(*args, **kwargs)

    
    # def hargaSatuan(self):
    #     return '{0:,}'.format(self.hargaSat)

    def __str__(self):
        # return self.nmrMat
        return '{}. {}'.format(self.id, self.descMat)
    
class InOutMaterial(models.Model):
    tglIn = models.DateField('Tanggal Masuk', blank=True)
    tglOut = models.DateField('Tanggal Keluar', blank=True)
    nmrMat = models.CharField('Nomor Material',max_length=200)
    descMat = models.CharField('Deskripsi Material',max_length=200)
    jmlMat = models.IntegerField('Jumlah Material')
    matIn = models.IntegerField('Material Masuk', default=0)
    matOut = models.IntegerField('Material Keluar', default=0)
    satuan = models.CharField('Satuan',max_length=200)
    hargaSat = models.IntegerField('Harga Satuan')
    random = models.IntegerField('Random')  
    # totalMat = models.IntegerField('Total Material')
    # noId = models.ForeignKey(InputModel, to_field='id', on_delete=models.CASCADE)

    # @property
    # def totMat(self):
    #     total = int(self.jmlMat) * int(self.hargaSat)
    #     return total

    # def save(self, *args, **kwargs):
    #     self.totalMat = self.totMat
    #     super(InOutMaterial, self).save(*args, **kwargs)

    def __str__(self):
        # return self.nmrMat
        return '{}. {}'.format(self.id, self.descMat)

    

from dataclasses import Field, field
from import_export import resources
from .models import InputModel
from import_export.fields import Field

class MaterialResource(resources.ModelResource):
    nmrMat = Field(attribute='nmrMat', column_name='Nomor Material')
    descMat = Field(attribute='descMat', column_name='Deskripsi Material')
    stock = Field(attribute='stock', column_name='Stock')
    satuan = Field(attribute='satuan', column_name='Satuan')
    hargaSat = Field(attribute='hargaSat', column_name='Harga Satuan')
    totalMat = Field(attribute='totalMat', column_name='Total Saldo')
    class Meta:
        model = InputModel
        fields = ['nmrMat','descMat','stock','satuan','hargaSat','totalMat']
        export_order = ['nmrMat','descMat','stock','satuan','hargaSat','totalMat']
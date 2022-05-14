from dataclasses import field
from pyexpat import model
from django.contrib import admin

# Register your models here.
from .models import InputModel, InOutMaterial
class InputAdmin(admin.ModelAdmin):
    list_display = ('id','nmrMat', 'descMat', 'tglMasuk', 'stock','satuan', 'hargaSat', 'totalMat')
    readonly_fields = ('totalMat','stock')

class InOutAdmin(admin.ModelAdmin):
    list_display = ('id','nmrMat', 'descMat', 'tglIn', 'tglOut','matIn','matOut','satuan', 'hargaSat')

admin.site.register(InputModel, InputAdmin)
admin.site.register(InOutMaterial, InOutAdmin)
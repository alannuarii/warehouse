from dataclasses import field
from pyexpat import model
from django import forms
from .models import InputModel, InOutMaterial
class InputForm(forms.ModelForm):
    class Meta:
        model = InputModel
        fields = [
            'nmrMat',
            'satuan',
            'descMat',
            'jmlMat',
            'hargaSat',
            'matIn',
            'matOut',
            'imgMat',
            'tglMasuk',
            'random',
        ]

class InOutForm(forms.ModelForm):
    class Meta:
        model = InOutMaterial
        fields = [
            'nmrMat',
            'satuan',
            'descMat',
            'jmlMat',
            'hargaSat',
            'tglIn',
            'tglOut',
            'matIn',
            'matOut',
            'random',
        ]


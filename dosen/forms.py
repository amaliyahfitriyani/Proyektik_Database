from dataclasses import fields
from django.forms import ModelForm
from django import forms
from dosen.models import Dosen

class FormDosen(ModelForm):
    class Meta:
        model = Dosen
        fields = ['no', 'nama', 'nidn', 'nip', 'jabatan', 'email']

       
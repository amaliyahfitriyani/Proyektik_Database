from dataclasses import fields
from django.forms import ModelForm
from django import forms
from staf.models import Staf

class FormStaf(ModelForm):
    class Meta:
        model = Staf
        fields = ['no', 'nama', 'nip', 'jabatan']
from django.db import models

# Create your models here.

class Dosen(models.Model):
    no = models.CharField(max_length=50)
    nama = models.CharField(max_length=50)
    nidn = models.CharField(max_length=50)
    nip = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=40)
    email = models.CharField(max_length=50)
    foto = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.no

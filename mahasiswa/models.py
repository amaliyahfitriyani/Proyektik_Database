from django.db import models

# Create your models here.

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=50)
    nama = models.CharField(max_length=70)
    ttl = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)
    foto = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.nim
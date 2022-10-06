from django.contrib import admin
from faperta.models import Faperta, Kelompok

# Register your models here.

class FapertaAdmin(admin.ModelAdmin):
    list_display: ['judul', 'penulis', 'penerbit']
    search_fields:['judul', 'penulis', 'penerbit']
    list_filter: ('kelompok_id',)
    list_per_page: 4

admin.site.register(Faperta, FapertaAdmin)
admin.site.register(Kelompok)

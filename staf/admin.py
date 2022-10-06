from django.contrib import admin
from staf.models import Staf

# Register your models here.

class StafAdmin(admin.ModelAdmin):
    list_display = ['no', 'nama', 'nip', 'jabatan']
    search_fields = ['no', 'nama']

admin.site.register(Staf, StafAdmin)

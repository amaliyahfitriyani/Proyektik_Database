from django.contrib import admin
from dosen.models import Dosen

# Register your models here.

class DosenAdmin(admin.ModelAdmin):
    list_display = ['no', 'nama', 'nidn', 'nip', 'jabatan', 'email', 'foto']
    search_fields = ['no', 'nama']

admin.site.register(Dosen, DosenAdmin)
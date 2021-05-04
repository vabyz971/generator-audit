from django.contrib import admin
from .models import Audit, Exploit

# Register your models here.

@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('name','author', 'readers')
    list_filter = ('author', 'readers', 'update_by')
    date_hierarchy = 'create_by'


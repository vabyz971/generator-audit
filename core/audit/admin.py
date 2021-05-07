from django.contrib import admin
from .models import Audit, Exploit

# Register your models here.


class ExploitInline(admin.TabularInline):
    model = Exploit


@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
    list_display = ('name','author', 'readers' ,'update_by','create_by')
    list_filter = ('author', 'readers', 'update_by')
    date_hierarchy = 'create_by'

    inlines = [ExploitInline]



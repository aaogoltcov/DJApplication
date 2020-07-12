from django.contrib import admin

# Register your models here.
from table.models import Header, File


@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    pass


@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    pass

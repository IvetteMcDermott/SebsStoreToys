from django.contrib import admin
from .models import Bookmarks


# Register your models here.

@admin.register(Bookmarks)
class Bookmarks(admin.ModelAdmin):
    list_display = ['id', 'user', 'ware', ]
    search_fields = ['user', 'ware', ]

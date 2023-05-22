from django.contrib import admin
from .models import NewsBlog

# Register your models here.


@admin.register(NewsBlog)
class Subcategory(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'description', 'source', 'date', )

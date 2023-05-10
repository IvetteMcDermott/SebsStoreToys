from django.contrib import admin
from .models import Review


# Register your models here.

@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ['id', 'ware', 'rating', 'body', 'author', 'date_created', ]
    search_fields = ['author', 'ware', 'rating', ]

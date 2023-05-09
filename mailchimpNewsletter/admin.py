from django.contrib import admin
from .models import Subscriber


# Register your models here.

@admin.register(Subscriber)
class Subscriber(admin.ModelAdmin):
    list_display = ['email', 'name', ]
    search_fields = ['email', ]

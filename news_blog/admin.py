from django.contrib import admin

# Register your models here.


@admin.register(NewsBlog)
class Subcategory(admin.ModelAdmin):
    list_filter = ('title',)
    list_display = ('title', 'description', 'source', 'date', )
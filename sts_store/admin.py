from django.contrib import admin
from .models import Ware, Category, Subcategory, WareImage

# Register your models here.


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)

    class Meta:
        verbose_name_plural = 'Categories'


@admin.register(Subcategory)
class Subcategory(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'category',)

    class Meta:
        verbose_name_plural = 'Subcategories'


@admin.register(Ware)
class Ware(admin.ModelAdmin):
    list_filter = ('subcategory',)
    search_fields = ['subcategory', 'name']
    list_display = ('id', 'name', 'sku', 'description', 'subcategory', 'price',
                    'height', 'width', 'length', 'new', 'clearance', )


@admin.register(WareImage)
class WareImage(admin.ModelAdmin):
    list_filter = ('ware',)
    search_fields = ['ware']
    list_display = ('id', 'ware', 'image', 'caption',)

from django.contrib import admin
from shop.models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','price','pimage','pdesc','category_id']

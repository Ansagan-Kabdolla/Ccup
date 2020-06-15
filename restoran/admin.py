from django.contrib import admin
from .models import *

admin.site.register(Category)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name','description','price','image','category')
    list_filter = ['price','category']
    search_fields = ['description']

@admin.register(Zakaz)
class ZakazAdmin(admin.ModelAdmin):
    list_display = ('name','email','date','number','table','get_foods')
    list_filter = ('date','table','foods')
    list_display_links = ['name']
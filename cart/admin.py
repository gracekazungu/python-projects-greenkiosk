from django.contrib import admin
from.models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display=("items_name","price","discount","quantity","description")

admin.site.register(Cart,CartAdmin)


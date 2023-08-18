from django.contrib import admin
from.models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('image','name','quantity','user', 'total_price','price','description')


admin.site.register(Cart,CartAdmin)


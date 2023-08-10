from django.contrib import admin
from.models import Cart

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    list_display = ('name','quantity','user', 'total_price','price')


admin.site.register(Cart,CartAdmin)

# image=models.ImageField()
    # name=models.CharField(max_length=32,default="")
    # price=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    # quantity=models.PositiveIntegerField(default=1)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    # products = models.ManyToManyField(Product)
    # total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # description=models.TextField()
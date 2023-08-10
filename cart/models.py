
from django.contrib.auth.models import User
from django.db import models
from inventory.models import Product

class Cart(models.Model):
    class Meta:
        verbose_name_plural = "cart"
    
    name=models.CharField(max_length=32,null=True)
    # image=models.ImageField(default="")
    price=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    quantity=models.PositiveIntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    # description=models.TextField()


    def __str__(self):
        return f"{self.user}'s Cart"



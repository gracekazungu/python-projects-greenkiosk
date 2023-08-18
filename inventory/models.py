from django.db import models

from vendor.models import Vendor

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=32,default="")
    price=models.DecimalField(max_digits=8,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to='inventory/images/')
    date_created=models.DateTimeField(auto_now_add=True)
    date_updated=models.DateTimeField(auto_now=True)
    stock=models.PositiveIntegerField()
    vendor=models.ForeignKey(Vendor,null=True,on_delete=models.CASCADE)


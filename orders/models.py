from django.db import models

# Create your models here.
# class Order(models.Model):
#     product=models.ForeignKey(product,on_delete=models.CASCADE)
#     customer=models.ForeignKey(customer,on_delete=models.CASCADE)
#     quantity=models.IntegerField(default=1)
#     price=models.IntegerField()
#     address=models.CharField(max_length=50,default='',blank=True)
#     phone=models.CharField(max_length=50,default='',blanck=True)
#     date=models.DateField(default=datetime.datetime.today)
#     status=models.BooleanField(default=False)
class Order(models.Model):
    order_number = models.CharField(max_length=32, unique=True)
    customer_name = models.CharField(max_length=32)
    customer_email = models.EmailField(max_length=255)
    customer_phone_number = models.CharField(max_length=15)
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=16, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ])
from django.db import models

# Create your models here.
# class Item(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.DecimalField(max_digits=8,decimal_places=2)

#     def __str__(self):
#         return self.name

# class OrderItem(models.Model):
#     item = models.CharField(max_length=32)
#     quantity = models.PositiveIntegerField(default=1)
#     user = models.CharField(max_length=32)
#     ordered = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.quantity} of {self.item.name}"

#     def get_total_item_price(self):
#         return self.quantity*self.item.price

#     def get_final_price(self):
#         return self.get_total_item_price()


# class Order(models.Model):
#     user = models.CharField(max_length=32)
#     items = models.CharField(max_length=50)
#     start_date = models.DateTimeField(auto_now=True)
#     ordered_date = models.DateTimeField()
#     ordered = models.BooleanField(default=False)
#     def __str__(self):
#         return self.user.username

#     def get_total(self):
#         total = 0
#         for order_item in self.items.all():
#             total += order_item.get_final_price()
#         return total


# Order-id
# Products
# Quantity
# Total-price
# Shipping-Information
# Order_history
# Order-date 
# Order-status

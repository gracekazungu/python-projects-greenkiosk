from django.db import models

# Create your models here.
class Delivery(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    distance = models.FloatField()
    def calculate_delivery_fee(self):
        if self.distance <= 5:
            return 10
        elif self.distance <= 10:
            return 20
        else:
            return 30
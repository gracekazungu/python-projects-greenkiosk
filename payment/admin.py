from django.contrib import admin
from.models import Payment
# Register your models here.

class PaymentAdmin(admin.ModelAdmin):
      display_list = ('PAYMENT_METHOD', 'STATUS_CHOICES', 'payment_method','amount','date','status','description')
admin.site.register(Payment,PaymentAdmin)

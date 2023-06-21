from django.db import models

# Create your models here.
class Cart(models.Model):
    items_name=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    number_of_items=models.PositiveIntegerField(default=1)
    discount=models.DecimalField(max_digits=8,decimal_places=2)
    quantity=models.PositiveIntegerField(default=1)
    description=models.TextField()
    def addProduct(request):
        user = request.user
        product_id = request.GET.get('product_id')
        product_cart = Product.objects.get(id=product_id)
        Cart(user=user, product=product_cart).save()
        return render(request, 'cart/addtocart.html')
    def delete_cart_item(request):
        cart_item_id = request.GET.get('cart_item_id')
        CartItem.objects.filter(cart__user=request.user.id,id=cart_item_id)
        return render(request, your_template)


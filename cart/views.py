# views.py
from django.shortcuts import render, redirect
from .models import Cart
from .forms import UploadCartForm
from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import Product
from django.contrib import messages

# from django.shortcuts import redirect, get_object_or_404


def upload_product_to_cart(request):
    if request.method=="POST":
        form=UploadCartForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=UploadCartForm()#creating an instance 
        
    return render(request,"cart/upload_product.html",{"form":form})

def view_cart(request):
    items=Cart.objects.all()
    return render(request,"cart/cart.html",{"items":items})
  

def product_delete(request, id):
    item = get_object_or_404(Cart, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect("product_list_view")

#     # If the request method is not POST, render a confirmation page.
    return render(request, 'cart/confirmation_page.html', {'item': item})

def product_update_view(request, id):
    item = Cart.objects.get(id=id)
    if request.method=="POST":
        form=UploadCartForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect("update_product",id=item.id)
    else:
        form=UploadCartForm(instance=item)
        return render(request,"cart/edit_product.html",{"form":form})
    


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    if request.method == 'POST':
        form = UploadCartForm(request.POST, initial={'product': product})
        if form.is_valid():
            form.save()
            messages.success(request, f"{product.name} added to cart.")
            return redirect("products_list_view")  # Redirect to products list
    else:
        form = UploadCartForm(initial={'product': product})
    
    return render(request, "cart/add_to_cart.html", {"form": form, "product": product})

def checkout(request):
    items = Cart.objects.all()
    total_price = sum(item.price * item.quantity for item in items)
    
    return render(request, "payment/checkout.html", {"items": items, "total_price": total_price})

    




    

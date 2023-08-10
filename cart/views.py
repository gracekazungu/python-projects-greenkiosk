# views.py
from django.shortcuts import render, redirect
from .models import Cart
from .forms import UploadProductForm
from django.shortcuts import render, get_object_or_404, redirect

# from django.shortcuts import redirect, get_object_or_404


def upload_product_to_cart(request):
    if request.method=="POST":
        form=UploadProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=UploadProductForm()#creating an instance 
        
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

def product_update_view(request,id):
    item=Cart.objects.get(id=id)
    if request.method=="POST":
        form=UploadProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect("product_update",id=item.id)
    else:
        form=UploadProductForm(instance=item)
        return render(request,"cart/edit_product.html",{"form":form})
    

from django.shortcuts import render
# render returns a  response
from.forms import ProductUploadForm
from inventory.models import Product
from django.shortcuts import render,redirect
from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def product_upload_view(request):
    if request.method=="POST":
        form=ProductUploadForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ProductUploadForm()#creating an instance 
        
    return render(request,"inventory/product_upload.html",{"form":form})



def products_list(request):
    products=Product.objects.all()
    return render(request,"inventory/products_list.html",{"products":products})


def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_detail.html",{"product":product})

def product_update_view(request,id):
    product=Product.objects.get(id=id)
    if request.method=="POST":
        form=ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
        return redirect("product_detail_view",id=product.id)
    else:
        form=ProductUploadForm(instance=product)
        return render(request,"inventory/edit_product.html",{"form":form})
    

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        product.delete()
        return redirect("products_list_view")

    # If the request method is not POST, render a confirmation page.
    return render(request, 'inventory/confirmation_page.html', {'product': product})

# def delete_product(request,id):
#     product=Product.objects.get(id=id)
#     product.delete()
#     return redirect("products_list_view")

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    request.session.setdefault('cart', [])
    cart = request.session['cart']
    cart.append({'id': product.id, 'name': product.name, 'price': str(product.price)})
    request.session.modified = True
    return redirect('product_list_view')

def view_cart(request):
    cart = request.session.get('cart', [])
    return render(request, 'cart/cart.html', {'cart': cart})

def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', [])
    for item in cart:
        if item['id'] == product.id:
            cart.remove(item)
            break
    request.session['cart'] = cart
    request.session.modified = True
    return redirect('view_cart')
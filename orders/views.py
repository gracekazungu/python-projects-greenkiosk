from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from orders.models import Order
from .forms import OrderUploadForm
def create_order(request):
    if request.method == 'POST':
        form = OrderUploadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderUploadForm()
    return render(request, 'order/create_order.html', {'form': form})
def edit_order(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    if request.method == 'POST':
        form = OrderUploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail', order_number=order_number)  # Redirect to order details page
    else:
        form = OrderUploadForm(instance=order)
    return render(request, 'orders/edit_order.html', {'form': form, 'order': order})



def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})
def order_detail(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    return render(request, 'orders/order_detail.html', {'order': order})
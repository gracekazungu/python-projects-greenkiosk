from django.urls import path
# urls.py
from . import views

urlpatterns = [
    # Other URL patterns...
    path('upload_product/', views.upload_product_to_cart, name='upload_product_to_cart'),
    path("cart_list/", views.view_cart,name="product_list_view"),
    path("product_delete/<int:id>",views.product_delete,name="product_delete"),
    path("product_update/<int:id>",views.product_update_view,name="update_product"),
    path("add_to_cart/<int:product_id>", views.add_to_cart, name="add_to_cart"),
    path("checkout/", views.checkout, name="checkout"),

]




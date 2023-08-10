from django.urls import path
# urls.py
from . import views

urlpatterns = [
    # Other URL patterns...
    path('upload_product/', views.upload_product_to_cart, name='upload_product_to_cart'),
    path("cart_list/", views.view_cart,name="product_list_view"),
    path("products/edit/<int:id>",views.product_update_view,name="product_update"),
    path("product_delete/<int:id>",views.product_delete,name="product_delete"),
    # path("product_detail/<int:id>",views.cart_detail,name="product_detail_view"),

]




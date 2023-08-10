from django.urls import path
from.views import product_upload_view
from.views import products_list
from.views import product_detail
from.views import product_update_view
from.views import delete_product
from.views import add_to_cart
from.views import view_cart
from.views import remove_from_cart



urlpatterns=[
    path("products/upload",product_upload_view,name="product_upload_view"),
    path("products/list",products_list,name="products_list_view"),
    path("products/<int:id>",product_detail,name="product_detail_view"),
    path("products/edit/<int:id>",product_update_view,name="product_update"),
    path("products/delete/<int:id>",delete_product,name="product_delete"),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view_cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]



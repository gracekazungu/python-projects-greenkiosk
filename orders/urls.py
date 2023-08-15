# order/urls.py
from django.urls import path
from .import views 

urlpatterns = [
    path("orders/create/", views.create_order, name="create_order"),
    path("orders/edit/<str:order_number>/",views.edit_order, name="edit_order"),
    path("orders/list/",views.order_list, name="order_list"),
    path("orders/detail/<str:order_number>/",views.order_detail, name="order_detail"),
]
from django.urls import path
# urls.py
from . import views
urlpatterns=[
    path("customers/upload",views.customer_upload_view,name="customer_upload_view"),
    path("customers/list",views.customer_list,name="customer_list_view"),
    path("customers/<int:id>",views.customer_detail,name="customer_detail_view"),
    path("customers/edit/<int:id>",views.customer_update_view,name="customer_update"),
    path("customers/delete/<int:id>",views.delete_customer,name="customer_delete"),
   
]
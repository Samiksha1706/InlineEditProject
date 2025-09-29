from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.product_list, name="product_list"),
    path("update/<int:pk>/", views.update_product, name="update_product"),
    
]

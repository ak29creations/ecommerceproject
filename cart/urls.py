from django.urls import path, include
from . import views
app_name='cart'
urlpatterns = [
    path('', views.cart_detail,name='cart_detail'),
    path('add/<int:product_id>', views.add_cart,name='add_cart'),
    path('remove_by_one/<int:product_id>', views.cart_remove,name='remove_by_one'),
    path('clear_cart/<int:product_id>', views.clear_cart,name='clear_cart'),
]
from django.urls import path
from . import views
app_name = 'shop'
urlpatterns = [
    path('', views.all_prod_cat,name='all_prod_cat'),
    path('shop/<slug:c_slug>/', views.all_prod_cat,name='products_by_category'),
    path('shop/<slug:c_slug>/<slug:p_slug>/', views.prod_details,name='prod_details'),
]
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('',views.home, name="home"),
    path('add_category/',views.add_category, name="add_category"),
    path('category_list/',views.category_list, name="category_list"),
    path('add/', views.add_product, name='add_product'),
    path('all/', views.product_list, name='product_list'),
]

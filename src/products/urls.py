from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('addproduct', views.test_add_user_form, name='test_add_user_form'),
    path('listproducts', views.listProducts, name='product-list'),
    path('getproduct/<int:ID>', views.viewProduct, name='viewproduct'),
    re_path(r'^updateproduct.*', views.updateProduct, name='updateproduct'),
    re_path(r'^deleteproduct.*', views.deleteProduct, name='deleteproduct'),
]
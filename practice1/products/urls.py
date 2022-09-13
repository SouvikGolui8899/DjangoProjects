from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.products_home_view, name='products_index'),
    path('create/', views.products_create_view, name='products_create'),
    path('<int:id>/', views.products_get_by_id_view, name='product_get_by_id')
]
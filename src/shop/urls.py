from django.urls import path

from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('products/<slug:category_slug>/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail')
]

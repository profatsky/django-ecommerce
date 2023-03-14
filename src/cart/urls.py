from django.urls import path
from . import views


urlpatterns = [
    path('', views.CartView.as_view(), name='cart_detail'),
    path('add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', views.CartDeleteView.as_view(), name='cart_remove')
]
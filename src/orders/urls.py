from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('<int:pk>', views.OrderDetailVIew.as_view(), name='order_detail')
]

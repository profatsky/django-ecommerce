from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, FormView

from .cart import Cart
from .forms import CartAddProductForm
from shop.models import Product


class CartAddFormView(FormView):
    form_class = CartAddProductForm

    def form_valid(self, form):
        cart = Cart(self.request)
        product = get_object_or_404(Product, id=self.kwargs['product_id'])
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        return redirect('cart_detail')

    def form_invalid(self, form):
        return redirect('cart_detail')


class CartView(ListView):
    template_name = 'cart/cart_detail.html'
    context_object_name = 'cart'

    def get_queryset(self):
        cart = Cart(self.request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={'quantity': item['quantity'], 'update': True}
            )
        return cart


class CartDeleteView(View):
    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.remove(get_object_or_404(Product, id=self.kwargs['product_id']))
        return redirect('cart_detail')

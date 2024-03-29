from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import send_checkout_notification


class OrderCreateView(CreateView):
    model = OrderItem
    form_class = OrderCreateForm
    template_name = 'orders/order_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

    def form_valid(self, form):
        order = form.save()
        cart = Cart(self.request)
        for item in cart:
            self.model.objects.create(
                order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity']
            )
        cart.clear()
        send_checkout_notification.delay(order.pk)
        self.request.session['order_id'] = order.pk
        return redirect(reverse('payment:process'))

import braintree
from django.views.generic import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView

from orders.models import Order


class PaymentProcessView(View):
    def post(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=request.session.get('order_id'))
        nonce = request.POST.get('payment_method_nonce', None)
        result = braintree.Transaction.sale({
            'amount': '{:.2f}'.format(order.get_total_cost()),
            'payment_method_nonce': nonce,
            'options': {
                'submit_for_settlement': True
            }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect('payment:done')
        else:
            return redirect('payment:canceled')

    def get(self, request, *args, **kwargs):
        order = get_object_or_404(Order, id=request.session.get('order_id'))
        client_token = braintree.ClientToken.generate()
        return render(request,
                      'payment/process.html',
                      {'order': order,
                       'client_token': client_token})


class PaymentDoneView(TemplateView):
    template_name = 'payment/done.html'


class PaymentCancelView(TemplateView):
    template_name = 'payment/canceled.html'

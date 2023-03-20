from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'surname', 'email', 'address', 'city', 'postal_code')

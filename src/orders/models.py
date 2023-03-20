from django.db import models

from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    surname = models.CharField(max_length=50, blank=True, verbose_name='Отчество')
    email = models.EmailField()
    address = models.CharField(max_length=250, verbose_name='Адрес')
    city = models.CharField(max_length=100, verbose_name='Город')
    postal_code = models.CharField(max_length=20, verbose_name='Почтовый индекс')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    paid = models.BooleanField(default=False, verbose_name='Оплачено')
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    def __str__(self):
        return f'Заказ №{self.pk}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE, verbose_name='Товар')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кол-во товаров')

    def __str__(self):
        return str(self.product)

    def get_cost(self):
        return self.price * self.quantity

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from orders.models import Order


@shared_task
def send_checkout_notification(order_id: int):
    """Задача отправки email уведомлений при успешном оформлении заказа"""
    order = Order.objects.get(pk=order_id)
    mail_sent = send_mail(
        subject=f'Заказ №{order.id}',
        message=f'{order.first_name}, \n\n'
                f'Вы успешно оформили заказ в нашем интернет-магазине',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[order.email])
    return mail_sent

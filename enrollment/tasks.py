from celery import shared_task
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page


@shared_task
def send_message(recipient: str):
    subject: str = 'Письмо Студенту'
    message: str = 'Это письмо доставлено вам'
    recipient_list: list = [recipient]

    send_mail(subject, message, None, recipient_list)

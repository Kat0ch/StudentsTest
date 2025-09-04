from celery import shared_task
from django.core.mail import send_mail


# TODO: можешь накатить статический анализатор какой-нить (ruff + precommit/lefthook)
@shared_task
def send_message(recipient: str,
                 subject: str,
                 message: str):
    recipient_list: list = [recipient]

    send_mail(subject, message, None, recipient_list)

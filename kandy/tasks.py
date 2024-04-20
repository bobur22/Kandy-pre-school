from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader

@shared_task
def send_mail_task(subject, message,  recipient_list, html_m):
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=False, html_message=html_m)
        return "Xabar Yuborildi"
    except:
        return "Xabar yuborilmadi"
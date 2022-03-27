from celery import shared_task
from django.core.mail import EmailMessage
from api.models import Advert


@shared_task
def create_task(email):
    users = Advert.objects.all()

    recipients = []

    for user in users:
        recipients.append(user.owner_email)

    msg = EmailMessage(
        subject=email['subject'],
        to=recipients,
        body=email['msg'],
    )
    msg.send()

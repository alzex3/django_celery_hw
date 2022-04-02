from celery import shared_task
from django.core.mail import EmailMessage
from more_itertools import chunked

from api.models import Advert


@shared_task
def create_task(new_email):
    emails_addresses = Advert.objects.all().values('owner_email')

    for email_address_chunk in chunked(emails_addresses, 15):

        recipients = []
        for email_address in email_address_chunk:
            recipients.append(email_address.get('owner_email'))

        msg = EmailMessage(
            subject=new_email['subject'],
            to=recipients,
            body=new_email['msg'],
        )
        msg.send()

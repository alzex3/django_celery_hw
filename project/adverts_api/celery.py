import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adverts_api.settings')

app = Celery(
    'adverts_api',
    backend=settings.CELERY_RESULT_BACKEND,
    broker=settings.CELERY_BROKER_URL,
)
app.autodiscover_tasks()

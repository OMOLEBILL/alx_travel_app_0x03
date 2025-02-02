import os
from listings.celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'alx_travel_app_0x03.settings')

app = Celery('alx_travel_app_0x03')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

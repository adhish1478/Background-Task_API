import os
from celery import Celery

# Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'background_tasks.settings')

# Create a Celery instance
app = Celery('background_tasks')

# Load settings from Django settings
app.config_from_object('django.conf:settings', namespace= 'CELERY')

# Load task modules from all registered Django apps
app.autodiscover_tasks()


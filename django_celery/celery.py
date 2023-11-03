import os
from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery.settings')

app = Celery('django_celery')

app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

@app.task
def add(x, y):
    return x + y    

# Method 2
# app.conf.beat_schedule = {
#     'every-10-seconds': {
#         'task': 'app.tasks.clear_session_cache',
#         'schedule': 10,
#         'args': ('1111', )
#     }
# }

# time scheduling with crontab
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'app.tasks.clear_session_cache',
        'schedule': crontab(minute='*/1'),
        'args': ('1111', )
    }
}
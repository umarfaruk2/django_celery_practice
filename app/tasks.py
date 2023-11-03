from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule
import json

@shared_task
def sub(x, y):
    sleep(5)
    return x + y

@shared_task(name='multiple_task')
def multi(x, y):
    sleep(2)
    return x * y

@shared_task
def clear_session_cache(id):
    print('Session cache cleared: ', {id})
    return id

@shared_task
def clear_redis_data(key):
    print('Redis data clear: ', {key})
    return key

def clear_rabbitMq_data(key):
    print('RabbitMQ data clear: ', {key})
    return key

# create schedule every 30 second
schedule, created = IntervalSchedule.objects.get_or_create(
    every = 30,
    period = IntervalSchedule.SECONDS,
)

PeriodicTask.objects.get_or_create(
    name = 'create RabbitMQ periodic task',
    task = 'app.tasks.clear_rabbitMq_data',
    interval = schedule,
    args = json.dumps(['hello'])
)

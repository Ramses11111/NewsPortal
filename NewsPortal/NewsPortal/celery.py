import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPortal.settings')

app = Celery('NewsPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'when_creating_post': {
        'task': 'news.tasks.notifi_about_new_post',
        'schedule': 30,
    },
}

app.conf.beat_schedule = {
    'when_week': {
        'task': 'news.tasks.notify_weekly',
        'schedule': crontab(minute=0, hour=8, day_of_week='monday'),
    },
}
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

app = Celery('django_celery_project')
app.conf.enable_utc = False

app.conf.update(timezone='Asia/Dhaka')

app.config_from_object(settings, namespace='CELERY')

#Celery Beat settings

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


# app.conf.beat_schedule = {
#     'add-every-30-seconds': {
#         'task': 'mainapp.tasks.generate_invoice',
#         'schedule': 30.0,
#         'args': (16, 16)
#     },
# }

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyProj.settings')

app = Celery('MyProj')
app.config_from_object(settings,namespace="CELERY")

#celery beat setting
app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')
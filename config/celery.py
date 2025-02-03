from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Установите переменную окружения для проекта Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создайте экземпляр Celery
app = Celery('config')

# Читайте конфигурацию из settings.py
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматически найдите задачи в приложениях
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

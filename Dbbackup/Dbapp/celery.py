import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_name.settings")
app = Celery("project_name")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
app.conf.beat_schedule = {
     # Everyday at 04:30
    "backup": {
        "task": "core.tasks.backup",
        "schedule": crontab(hour=2, minute=00)
    },
}
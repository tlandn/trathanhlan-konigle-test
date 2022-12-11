import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unity_project.settings")

app = Celery("unity_project")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "send_statistics_email_monday": {
        "task": "unity.tasks.send_statistics_email",
        "schedule": crontab(hour=1, minute=30, day_of_week=1),
        "args": (),
    },
    "send_statistics_email_wednesday": {
        "task": "unity.tasks.send_statistics_email",
        "schedule": crontab(hour=1, minute=30, day_of_week=3),
        "args": (),
    },
}

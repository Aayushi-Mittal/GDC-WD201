from datetime import timedelta
from django.core.mail import send_mail
from celery.decorators import periodic_task
from task_manager.celery import app
from tasks.models import Task
import time


@periodic_task(run_every=timedelta(seconds=30))
def send_email_reminder():
    print("Starting to process Emails")

    for user in user.objects.all():
        pending_qs = Task.objects.filter(user=user, completed=False, deleted=False)
        email_content = f"You have {pending_qs.count()} Pending Tasks"
        send_mail(
            "Pending Tasks from task manager",
            "tasks@task_manager.org",
        )
        print("Email sent!")


@app.task
def test_background_jobs():
    print("This is from the bg.")
    for i in range(10):
        time.sleep(1)
        print(1)

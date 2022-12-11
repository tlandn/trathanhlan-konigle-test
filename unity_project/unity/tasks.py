from datetime import date

from celery import shared_task
from django.core.mail import send_mail

from unity_project.helpers.email_utils import (
    get_emails_all,
    get_emails_new,
    get_emails_unsubcribed,
)


@shared_task
def send_statistics_email():
    today = date.today()
    emails_subcribed = get_emails_all()
    emails_unsubcribed = get_emails_unsubcribed()
    emails_new = get_emails_new(today.year, today.month)

    subject = f"Your email statistics"
    message = (
        f"Hi,\n"
        f"Here are your email statistics:\n"
        f"Total emails: {emails_subcribed['emails_subscribed_count']}, new email this month: {emails_new['emails_new_count']}, unsubscribed: {emails_unsubcribed['emails_unsubscribed_count']}"
    )
    mail_sent = send_mail(
        subject, message, "admin@gmail.com", ["seller_email@gmail.com"]
    )
    return mail_sent

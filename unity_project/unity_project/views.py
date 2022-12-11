from datetime import date, datetime

from django.shortcuts import render

from .helpers.email_utils import get_emails_all, get_emails_new, get_emails_unsubcribed


def render_home(request):
    today = date.today()
    month_year_formatted = today.strftime("%B %Y")
    emails_subcribed = get_emails_all()
    emails_unsubcribed = get_emails_unsubcribed()
    emails_new = get_emails_new(today.year, today.month)
    context = {
        "month_year": month_year_formatted,
        "emails_subscribed": emails_subcribed["emails_subscribed"],
        "emails_subscribed_count": emails_subcribed["emails_subscribed_count"],
        "emails_new_count": emails_new["emails_new_count"],
        "emails_unsubscribed_count": emails_unsubcribed["emails_unsubscribed_count"],
    }
    return render(request, "home.html", context)

from unity.models import Email
from unity.serializers import EmailSerializer


def get_emails_all():
    emails_subscribed = Email.objects.filter()
    emails_serializer = EmailSerializer(emails_subscribed, many=True).data
    return {
        "emails_subscribed": emails_serializer,
        "emails_subscribed_count": emails_subscribed.count(),
    }


def get_emails_unsubcribed():
    emails_unsubscribed = Email.objects.filter(unsubscribed_at__isnull=False)
    return {"emails_unsubscribed_count": emails_unsubscribed.count()}


def get_emails_new(year, month):
    emails_new = Email.objects.filter(created_at__year=year, created_at__month=month)
    return {"emails_new_count": emails_new.count()}

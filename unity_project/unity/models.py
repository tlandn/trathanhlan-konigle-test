from django.db import models


class Email(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verified_at = models.DateTimeField(null=True)
    unsubscribed_at = models.DateTimeField(null=True)

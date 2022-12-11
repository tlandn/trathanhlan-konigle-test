from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Email


class EmailSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField(read_only=True)
    created_at_humanize = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Email
        fields = ["email", 'created_at', "verified_at", "unsubscribed_at", "status", "created_at_humanize"]

    def get_status(self, object):
        if object.unsubscribed_at:
            return 'Unsubscribed'
        elif object.verified_at:
            return 'Verified'   
        return 'Subscribed'
            
    def get_created_at_humanize(self, object):
        return naturaltime(object.created_at)

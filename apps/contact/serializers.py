from rest_framework import serializers
from .models import Contact, Lead

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "phone",
            "email",
            "location",
            "maps_url",
            "instagram",
            "facebook",
        ]


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
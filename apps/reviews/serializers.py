from rest_framework import serializers
from .models import Review

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = [
            "id",
            "name",
            "type",
            "photo",
            "video",
            "description",
            "created_at",
        ]

    def validate(self, data):
        review_type = data.get("type")

        if not data.get("photo"):
            raise serializers.ValidationError({
                "photo": "Photo is required."
            })

        if review_type == "video" and not data.get("video"):
            raise serializers.ValidationError({
                "video": "Video is required for video type."
            })

        if review_type == "text":
            data["video"] = None

        return data
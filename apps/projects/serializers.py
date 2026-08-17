from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "image",
            "description",
            "location",
            "year",
            "category",
            "category_name",
            "created_at",
        ]
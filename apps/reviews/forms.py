from django import forms
from .models import Review


class ReviewAdminForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = [
            "name",
            "type",
            "photo",
            "video",
            "description",
        ]

    def clean(self):
        cleaned_data = super().clean()

        review_type = cleaned_data.get("type")
        photo = cleaned_data.get("photo")
        video = cleaned_data.get("video")

        if not photo:
            self.add_error(
                "photo",
                "Photo is required."
            )

        if review_type == "video" and not video:
            self.add_error(
                "video",
                "Video is required for Video review."
            )

        if review_type == "text":
            cleaned_data["video"] = None

        return cleaned_data
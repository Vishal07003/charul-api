from django.contrib import admin
from django.utils.html import format_html

from .models import Review
from .forms import ReviewAdminForm


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    form = ReviewAdminForm

    class Media:
        js = ("admin/reviews.js",)

    list_display = (
        "id",
        "name",
        "type",
        "photo_preview",
        "created_at",
    )

    list_filter = (
        "type",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "-created_at",
    )

    readonly_fields = (
        "photo_preview",
    )

    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" width="80" height="60" '
                'style="object-fit:cover;border-radius:6px;" />',
                obj.photo.url,
            )

        return "No photo"

    photo_preview.short_description = "Photo"
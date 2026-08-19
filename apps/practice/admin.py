from django.contrib import admin
from django.utils.html import format_html
from .models import Practice

@admin.register(Practice)
class PracticeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "image_preview",
    )

    search_fields = (
        "title",
        "description",
    )

    readonly_fields = (
        "image_preview",
    )

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="70" '
                'style="object-fit: cover; border-radius: 6px;" />',
                obj.image.url,
            )
        return "No image"

    image_preview.short_description = "Image"
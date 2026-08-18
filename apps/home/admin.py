from django.contrib import admin
from .models import Hero


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_preview",
        "created_at",
    )

    ordering = ("-created_at",)

    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="120" height="70" style="object-fit: cover;" />'
        return "No image"

    image_preview.allow_tags = True
    image_preview.short_description = "Preview"
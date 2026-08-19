from django.contrib import admin
from .models import Process


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "step",
        "title",
    )

    search_fields = (
        "title",
        "description",
    )

    ordering = (
        "step",
    )
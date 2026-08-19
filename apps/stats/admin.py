from django.contrib import admin
from .models import Stat

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "value",
        "label",
    )

    search_fields = (
        "value",
        "label",
    )

    ordering = ("id",)
from django.contrib import admin
from .models import Contact, Lead

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone",
        "email",
        "location",
    )

    search_fields = (
        "phone",
        "email",
        "location",
    )


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
    )
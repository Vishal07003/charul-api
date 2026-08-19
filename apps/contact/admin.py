from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "phone",
        "email",
        "studio",
    )

    search_fields = (
        "phone",
        "email",
        "studio",
    )
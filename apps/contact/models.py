from django.db import models

class Contact(models.Model):
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    maps_url = models.URLField(
        blank=True,
        null=True,
        help_text="Google Maps embed link (Share > Embed a map > copy the src URL)."
    )

    instagram = models.URLField(
        blank=True,
        null=True
    )

    facebook = models.URLField(
        blank=True,
        null=True
    )

    def __str__(self):
        return "Company Contact"


class Lead(models.Model):
    name = models.CharField(max_length=255)

    email = models.EmailField(blank=True, null=True)

    phone = models.CharField(max_length=20, blank=True, null=True)

    message = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
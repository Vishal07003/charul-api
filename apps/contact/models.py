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

    studio = models.CharField(
        max_length=255,
        blank=True,
        null=True
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
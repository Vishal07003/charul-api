from django.db import models


class Contact(models.Model):
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
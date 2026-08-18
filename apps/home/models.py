from django.db import models


class Hero(models.Model):
    image = models.ImageField(
        upload_to="hero/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Hero Image {self.id}"
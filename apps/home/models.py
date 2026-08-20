from django.db import models


class Home(models.Model):
    image = models.ImageField(
        upload_to="home/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"Home Page Image {self.id}"
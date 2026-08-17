from django.db import models


class Review(models.Model):
    name = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to="reviews/",
        blank=True,
        null=True
    )

    rating = models.PositiveIntegerField()

    comment = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} - {self.rating}"
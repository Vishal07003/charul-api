from django.db import models


class Review(models.Model):

    TYPE_CHOICES = [
        ("text", "Text"),
        ("video", "Video"),
    ]

    name = models.CharField(max_length=255)

    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES
    )

    photo = models.ImageField(
        upload_to="reviews/photos/",
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to="reviews/videos/",
        blank=True,
        null=True
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name
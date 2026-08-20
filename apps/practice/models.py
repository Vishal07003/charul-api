from django.db import models


class Practice(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    image = models.ImageField(
        upload_to="practice/",
        blank=True,
        null=True
    )

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title
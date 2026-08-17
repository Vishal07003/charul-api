from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True
    )

    description = models.TextField()

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="services"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
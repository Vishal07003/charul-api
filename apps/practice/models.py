from django.db import models


class Practice(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    image = models.ImageField(
        upload_to="practice/",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
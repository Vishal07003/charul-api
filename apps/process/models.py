from django.db import models


class Process(models.Model):
    step = models.PositiveIntegerField()

    title = models.CharField(
        max_length=255
    )

    description = models.TextField()

    class Meta:
        ordering = ["step"]

    def __str__(self):
        return f"{self.step}. {self.title}"
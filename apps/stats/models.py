from django.db import models


class Stat(models.Model):
    value = models.CharField(max_length=50)

    label = models.CharField(max_length=255)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.value} - {self.label}"
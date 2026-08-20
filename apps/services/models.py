from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name
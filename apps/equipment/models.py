from django.db import models


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to="equipment/")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.name

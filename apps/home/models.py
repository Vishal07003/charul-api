from django.db import models
class Hero(models.Model):
    title = models.CharField(max_length=255)
    subtitle = models.TextField(
        blank=True
    )
    image = models.ImageField(
        upload_to="hero/"
    )
    button_text = models.CharField(
        max_length=100,
        blank=True
    )
    button_link = models.CharField(
        max_length=255,
        blank=True
    )
    def __str__(self):
        return self.title
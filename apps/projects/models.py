from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="projects/")
    description = models.TextField()
    location = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.CASCADE,
        related_name="projects"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
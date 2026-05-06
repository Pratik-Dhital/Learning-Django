from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    receipe_image = models.ImageField(upload_to="receipe/")

    def __str__(self):
        return self.name
from django.db import models


class GeneratedImage(models.Model):
    gender = models.CharField(max_length=6)
    primary_color = models.CharField(max_length=7)
    props = models.CharField(max_length=100)
    image = models.ImageField(upload_to="generated_images/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gender} - {self.primary_color} - {self.props}"

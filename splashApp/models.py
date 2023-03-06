from django.db import models

class Splash(models.Model):
    label = models.CharField(max_length=200)
    image_url = models.URLField()
    image = models.ImageField(upload_to="images")

    def __str__(self):
        return self.label
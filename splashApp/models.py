from django.db import models

class Splash(models.Model):
    label = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)
    picture = models.ImageField(upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.label
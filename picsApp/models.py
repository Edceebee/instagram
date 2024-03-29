from django.db import models


class Photo(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name

from django.db import models

class Attractions(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    duration = models.TextField()
    min_age = models.IntegerField()

    def __str__(self):
        return self.name
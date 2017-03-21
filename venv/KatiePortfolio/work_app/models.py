from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=40)
    image = models.CharField(max_length=200)

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    urls = models.URLField(blank=True)

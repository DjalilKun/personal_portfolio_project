from django.db import models
from django.utils import timezone 

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=350)
    urls = models.URLField(blank=True)

def __str__(self):
        return self.name

class Meta:
        db_table = 'state'
        # Add verbose name
        verbose_name = 'State List'

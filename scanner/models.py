from django.db import models

# Create your models here.
class Note(models.Model):
    image = models.CharField(max_length=2000000)
    created_at = models.DateTimeField(auto_now_add=True)
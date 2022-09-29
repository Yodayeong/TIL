from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.CharField(max_length = 80)
    completed = models.BooleanField(default=False)
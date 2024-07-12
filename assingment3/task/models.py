from django.db import models
from catagory.models import Catagory

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    completed=models.BooleanField()
    date=models.DateTimeField()
    catagory=models.ManyToManyField(Catagory)

    def __str__(self):
        return self.title


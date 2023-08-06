from django.db import models

CHOICES = [
    ('Pending','pending'),
    ("In Progress", "in progress"),
    ( 'Completed',"completed")
]

# Create your models here.
class Task(models.Model):
    name = models.CharField('Task Name', max_length=20)
    status = models.CharField(max_length=200, choices=CHOICES, blank=True)
    finished = models.BooleanField(default=False)
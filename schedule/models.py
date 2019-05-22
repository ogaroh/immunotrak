from django.db import models

# Create your models here.
class Schedule (models.Model):
    date = models.DateField(null=False)
    child = models.DateTimeField(null=False)
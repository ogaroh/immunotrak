from django.db import models
from trak.models import Child, Vaccine


# Create your models here

# Schedule model
class Schedule (models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

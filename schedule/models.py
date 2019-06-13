from django.db import models
from trak.models import Child, Vaccine


# Create your models here

# Schedule model
class Schedule (models.Model):
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, related_name='Schedules')

    def __str__(self):
        return self.type
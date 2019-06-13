from django.db import models

# Create your models here.


# Vaccines model
class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# parent model
class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    id_number = models.DecimalField(decimal_places=0, max_digits=50)
    phone_number = models.DecimalField(decimal_places=0, max_digits=10)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


# child model
class Child(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=False)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# counties model
class County(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()
    vaccinations = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

# location model
class Location(models.Model):
    county = models.CharField(max_length=50)
    vaccinations = models.IntegerField()  # insert foreign from vaccination model

    def __str__(self):
        return self.county

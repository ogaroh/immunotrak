from django.db import models

# Create your models here.


# Vaccines model
class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)


# child model
class Child(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField(null=False)
    child_id = models.IntegerField()
    # parent = models.ForeignKey(Parent) # insert from parent model

    def __str__(self):
        return self.first_name


# parent model
class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    parent_id = models.DecimalField(decimal_places=0, max_digits=50)
    # children = models.ForeignKey(Child) # insert from child model



# location model
class Location(models.Model):
    county = models.CharField(max_length=50)
    vaccinations = models.IntegerField() # insert foreign from vaccination model
    

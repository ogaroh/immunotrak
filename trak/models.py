from django.db import models
from django.forms import ModelForm

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

COUNTY_CHOICES = [
    ('Mombasa County', 'Mombasa'),
    ('Kwale County', 'Kwale'),
    ('Kilifi County', 'Kilifi'),
    ('Tana River County', 'Tana River'),
    ('Lamu County', 'Lamu'),
    ('Taita Taveta County', 'Taita Taveta'),
    ('Garissa County', 'Garissa'),
    ('Wajir County', 'Wajir'),
    ('Mandera County', 'Mandera'),
    ('Marsabit County', 'Marsabit'),
    ('Isiolo County', 'Isiolo'),
    ('Meru County', 'Meru'),
    ('Tharaka Nithi County', 'Tharaka Nithi'),
    ('Embu County', 'Embu'),
    ('Kitui County', 'Kitui'),
    ('Machakos County', 'Machakos'),
    ('Makueni County', 'Makueni'),
    ('Nyandarua County', 'Nyandarua'),
    ('Nyeri County', 'Nyeri'),
    ('Kirinyaga County', 'Kirinyaga'),
    ("Murang'a County", "Murang'a"),
    ('Kiambu County', 'Kiambu'),
    ('Turkana County', 'Turkana'),
    ('West Pokot County', 'West Pokot'),
    ('Samburu County', 'Samburu'),
    ('Trans-Nzoia County', 'Trans-Nzoia'),
    ('Uasin Gishu County', 'Uasin Gishu'),
    ('Elgeyo Marakwet County', 'Elgeyo Marakwet'),
    ('Nandi County', 'Nandi'),
    ('Baringo County', 'Baringo'),
    ('Laikipia County', 'Laikipia'),
    ('Nakuru County', 'Nakuru'),
    ('Narok County', 'Narok'),
    ('Kajiado County', 'Kajiado'),
    ('Kericho County', 'kericho'),
    ('Bomet County', 'Bomet'),
    ('Kakamega County', 'Kakamega'),
    ('Vihiga County', 'Vihiga'),
    ('Bungoma County', 'Bungoma'),
    ('Busia County', 'Busia'),
    ('Siaya County', 'Siaya'),
    ('Kisumu County', 'Kisumu'),
    ('Homa Bay County', 'Homa Bay'),
    ('Migori County', 'Migori'),
    ('Kisii County', 'Kisii'),
    ('Nyamira County', 'Nyamira'),
    ('Nairobi County', 'Nairobi'),
]

# Create your models here
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
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


# location model
class Location(models.Model):
    county = models.CharField(max_length=20, choices=COUNTY_CHOICES)
    vaccinations = models.IntegerField()  # insert foreign from vaccination model

    def __str__(self):
        return self.county

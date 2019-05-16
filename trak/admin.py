from django.contrib import admin
from .models import Vaccine, Child, Parent, Location

admin.site.site_header = "ImmunoTrak"
admin.site.site_title = "ImmunoTrak"

# Register your models here.
admin.site.register(Vaccine)
admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Location)
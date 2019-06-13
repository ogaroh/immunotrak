from django.contrib import admin
from .models import Vaccine, Child, Parent, Location
import schedule.admin
import charts.admin

admin.site.site_header = "ImmunoTrak"
admin.site.site_title = "ImmunoTrak"

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'quantity', 'available')
    list_display_links = ('id', 'description', 'quantity','available')
    search_fields = ('id', 'name')
    list_per_page = 30


# Register your models here.
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(Child)
admin.site.register(Parent)
admin.site.register(Location)

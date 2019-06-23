from django.contrib import admin
from .models import Vaccine, Child, Parent, Location, County
import schedule.admin
import charts.admin
import stats.admin

admin.site.site_header = "ImmunoTrak"
admin.site.site_title = "ImmunoTrak"

class VaccineAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'quantity', 'available')
    list_display_links = ('id', 'description', 'quantity','available')
    search_fields = ('id', 'name')
    list_per_page = 30


class ParentAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'id_number', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name','id_number', 'phone_number')
    search_fields = ('id', 'first_name', 'last_name', 'id_number', 'phone_number')
    list_per_page = 40



class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'dob', 'parent')
    list_display_links = ('id', 'first_name', 'last_name','dob', 'parent')
    search_fields = ('id', 'first_name', 'last_name', 'dob', 'parent')
    list_per_page = 40  


# Register your models here.
admin.site.register(Vaccine, VaccineAdmin)
admin.site.register(Child, ChildAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Location)
admin.site.register(County)

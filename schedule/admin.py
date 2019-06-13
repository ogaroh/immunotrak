from django.contrib import admin
from .models import Schedule


# modify outlines in admin page
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id', 'vaccine', 'child', 'date', 'description')
    list_display_links = ('id', 'vaccine', 'child','date')
    search_fields = ('id','description')
    list_per_page = 30


# Register your models here.
admin.site.register(Schedule, ScheduleAdmin)
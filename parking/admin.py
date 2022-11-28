from django.contrib import admin
from .models import Location, Section, Spot, Motion

# Register your models here.
admin.site.register(Location)
admin.site.register(Section)

# default admin site with custom form
class SpotAdmin(admin.ModelAdmin):
    list_display = ('id', 'section', 'row', 'column', 'status')
    search_fields = ("status__icontains",)

admin.site.register(Spot, SpotAdmin)
admin.site.register(Motion)
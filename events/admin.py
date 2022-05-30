from django.contrib import admin

from .models import Event, Location, Participant

# Register your models here.

class EventAdmin(admin.ModelAdmin):
  list_display = ('title', 'date', 'location')
  list_filter = ('location', 'date')
  prepopulated_fields = {'slug': ('title', )}


admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(Participant)
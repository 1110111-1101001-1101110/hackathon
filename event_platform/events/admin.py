
from django.contrib import admin
from .models import Event, Rating

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time', 'location')
    list_filter = ('category', 'date_time')

class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'score', 'comment')
    search_fields = ('user__username', 'event__title')
    list_filter = ('score',)


admin.site.register(Event, EventAdmin)
admin.site.register(Rating, RatingAdmin)

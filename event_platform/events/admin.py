# events/admin.py
from django.contrib import admin
from .models import Event, Rating

class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time', 'location')  # Используйте 'date_time', а не 'date'
    list_filter = ('category', 'date_time')  # Также используем 'date_time' в фильтре

class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'score', 'comment')
    search_fields = ('user__username', 'event__title')
    list_filter = ('score',)

# Регистрируем модели в админке
admin.site.register(Event, EventAdmin)
admin.site.register(Rating, RatingAdmin)

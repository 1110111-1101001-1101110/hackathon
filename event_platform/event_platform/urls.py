

from django.contrib import admin
from django.urls import path, include
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.event_list, name='event_list'),
    path('events/', include('events.urls')),
]

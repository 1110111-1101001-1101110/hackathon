# event_platform/urls.py

from django.contrib import admin
from django.urls import path, include
from events import views  # Подключаем views из приложения "events"

urlpatterns = [
    path('admin/', admin.site.urls),  # Путь для админки
    path('', views.event_list, name='event_list'),  # Главная страница с мероприятиями
    path('events/', include('events.urls')),  # Все URL для приложения events
]

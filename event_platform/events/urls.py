# events/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),  # Главная страница для мероприятий
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),  # Страница с деталями мероприятия
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
]

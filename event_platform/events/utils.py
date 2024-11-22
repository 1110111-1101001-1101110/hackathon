# events/utils.py
from .models import Event, Rating  # Импортируем модели Event и Rating

def recommended_events(user):
    # Проверяем, аутентифицирован ли пользователь
    if not user.is_authenticated:
        return Event.objects.none()

    # Получаем все категории, по которым пользователь оставил рейтинги
    user_categories = Rating.objects.filter(user=user).values_list('event__category', flat=True).distinct()

    # Если у пользователя нет оценок, возвращаем пустой QuerySet
    if not user_categories.exists():
        return Event.objects.none()

    # Возвращаем мероприятия из этих категорий, исключая уже оценённые пользователем
    return Event.objects.filter(category__in=user_categories).exclude(ratings__user=user).distinct()

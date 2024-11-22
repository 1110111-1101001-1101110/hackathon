from django.db import models
from django.contrib.auth.models import User


# Категория мероприятия (например, наука, спорт, музыка и т.д.)
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Модель мероприятия
class Event(models.Model):
    title = models.CharField(max_length=255)  # Название мероприятия
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория мероприятия
    date_time = models.DateTimeField()  # Дата и время мероприятия
    location = models.CharField(
        max_length=50,
        choices=[('online', 'Online'), ('offline', 'Offline')],
        default='offline'
    )  # Локация (онлайн или оффлайн)
    description = models.TextField()  # Описание мероприятия

    def __str__(self):
        return self.title


# Модель рейтинга мероприятия (оценки и комментарии)
class Rating(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')  # Связь с мероприятием
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с пользователем
    score = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])  # Оценка мероприятия
    comment = models.TextField(blank=True, null=True)  # Комментарий к мероприятию (необязательный)

    def __str__(self):
        return f"Rating for {self.event.title} by {self.user.username}"

    class Meta:
        unique_together = ('user', 'event')  # Ограничение: один пользователь может оставить один отзыв на одно событие


# Функция для получения рекомендованных мероприятий
def recommended_events(user):
    if not user.is_authenticated:
        return Event.objects.none()  # Пустой QuerySet для неавторизованных пользователей

    # Получаем список ID категорий, на которые пользователь уже оставлял рейтинг
    user_categories = Rating.objects.filter(user=user).values_list('event__category', flat=True).distinct()

    if not user_categories:  # Если пользователь не оценивал события, возвращаем пустой QuerySet
        return Event.objects.none()

    # Возвращаем мероприятия из категорий, которые оценивал пользователь, исключая уже оцененные им
    return Event.objects.filter(category__in=user_categories).exclude(ratings__user=user).distinct()

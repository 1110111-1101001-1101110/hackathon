
from .models import Event, Rating

def recommended_events(user):

    if not user.is_authenticated:
        return Event.objects.none()


    user_categories = Rating.objects.filter(user=user).values_list('event__category', flat=True).distinct()


    if not user_categories.exists():
        return Event.objects.none()


    return Event.objects.filter(category__in=user_categories).exclude(ratings__user=user).distinct()

from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Event(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    location = models.CharField(
        max_length=50,
        choices=[('online', 'Online'), ('offline', 'Offline')],
        default='offline'
    )
    description = models.TextField()

    def __str__(self):
        return self.title



class Rating(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Rating for {self.event.title} by {self.user.username}"

    class Meta:
        unique_together = ('user', 'event')



def recommended_events(user):
    if not user.is_authenticated:
        return Event.objects.none()


    user_categories = Rating.objects.filter(user=user).values_list('event__category', flat=True).distinct()

    if not user_categories:  
        return Event.objects.none()

    
    return Event.objects.filter(category__in=user_categories).exclude(ratings__user=user).distinct()

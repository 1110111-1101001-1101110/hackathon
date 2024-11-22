from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Event, Rating
from .forms import RatingForm, UserRegistrationForm
from .utils import recommended_events
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout



def event_list(request):
    events = Event.objects.all() 
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)  
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, event=event).first()

    if request.method == 'POST' and request.user.is_authenticated:
        form = RatingForm(request.POST)
        if form.is_valid():
            score = form.cleaned_data['score']
            comment = form.cleaned_data['comment']

            rating, created = Rating.objects.update_or_create(
                user=request.user, event=event,
                defaults={'score': score, 'comment': comment}
            )
            return redirect('event_detail', event_id=event.id)
    else:
        form = RatingForm(instance=user_rating)

    return render(request, 'events/event_detail.html', {
        'event': event,
        'user_rating': user_rating,
        'form': form
    })


@login_required
def profile(request):

    ratings = Rating.objects.filter(user=request.user)
    

    recommended = recommended_events(request.user)


    return render(request, 'events/profile.html', {
        'ratings': ratings,
        'recommended': recommended
    })


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('event_list')
    else:
        form = AuthenticationForm()

    return render(request, 'events/login.html', {'form': form})


def register_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('event_list')

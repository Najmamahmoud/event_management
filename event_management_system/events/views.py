
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EventForm, CustomUserCreationForm
from .models import Event

def home(request):
    return render(request, 'events/home.html')

def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def list_events(request):
    events = Event.objects.all()
    return render(request, 'events/list_events.html', {'events': events})

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'events/event_detail.html', {'event': event})

def edit_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('list_events')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('list_events')
    return render(request, 'events/delete_event.html', {'event': event})

def user_profile(request):
    return render(request, 'registration/profile.html')

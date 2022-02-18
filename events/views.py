from django.shortcuts import render
from django.utils import timezone

from .models import Event
from blog.models import Post


def EventsView(request):
    today = timezone.now() + timezone.timedelta(days=1)
    end = today + timezone.timedelta(weeks=64)
    upcoming_events = Event.objects.filter(date__range=[today, end])
    events = Event.objects.all()
    post_list = Post.objects.all()[:3]
    context = {"upcoming_events": upcoming_events, "events": events, "posts": post_list}
    return render(request, "events/events.html", context)

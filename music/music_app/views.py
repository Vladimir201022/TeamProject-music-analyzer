# music/views.py
from django.shortcuts import render
from .models import Genre, Track, Chart

def popular_genres(request):
    genres = Genre.objects.all()
    return render(request, 'popular.html', {'genres': genres})

def trends_and_forecasts(request):
    tracks = Track.objects.all()
    charts = Chart.objects.all().order_by('rank')
    return render(request, 'trends.html', {'tracks': tracks, 'charts': charts})

def index(request):
    return render(request, 'index.html')

def artists(request):
    artists = Track.objects.values('artist').distinct()
    return render(request, 'artists.html', {'artists': artists})

def about(request):
    return render(request, 'about.html')

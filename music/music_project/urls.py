# music_project/urls.py
from django.contrib import admin
from django.urls import path
from music_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('popular.html/', views.popular_genres, name='popular_genres'),
    path('trends.html/', views.trends_and_forecasts, name='trends_and_forecasts'),
    path('artists.html/', views.artists, name='artists'),
    path('about.html/', views.about, name='about'),
]

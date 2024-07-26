# music_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('popular/', views.popular_genres, name='popular_genres'),
    path('trends/', views.trends_and_forecasts, name='trends_and_forecasts'),
    path('artists/', views.artists, name='artists'),
    path('about/', views.about, name='about'),
]

from django.urls import path

from music_db.views import *

urlpatterns = [
    path('music/', MusicListView.as_view()),
    path('music-create/', MusicCreateView.as_view()),
    path('music-update/<int:pk>/', MusicUpdateView.as_view()),
    path('music-detail/<int:pk>/', MusicDetailView.as_view()),
    path('music-delete/<int:pk>/', MusicDeleteView.as_view())
    ]
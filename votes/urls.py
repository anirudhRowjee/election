from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='vote_mainmenu'),
    path('vote/', views.vote, name='vote'),
    path('cluster/', views.cluster, name='cluster'),
]


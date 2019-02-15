from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='vote_mainmenu'),
    path('vote/<int:booth_id>/', views.vote, name='vote'),
    path('cluster/<int:cluster_id>/', views.cluster, name='cluster'),
]


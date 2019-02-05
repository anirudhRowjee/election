from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('voters/', views.populate_voters, name='voter_ops')
]

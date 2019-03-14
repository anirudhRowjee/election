from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login_electionadmin'),
    path('home/', views.home, name='home_electionadmin'),
    path('logout/', views.logout, name='logout_a'),
    path('voters/', include('voters.urls'), name='voters'),
    path('elections/', include('elections.urls'), name='elections'),
    path('candidates/', include('candidates.urls'), name='candidates'),
    path('clusters/', include('clustermaster.urls'), name='clustermaster'),
]

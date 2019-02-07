from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('voters/', include('voters.urls'), name='voters'),
    path('elections/', include('elections.urls'), name='elections'),
    path('candidates/', include('candidates.urls'), name='candidates'),
]

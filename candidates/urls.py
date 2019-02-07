from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('all/', views.view_all, name='view_all'),
    path('add/', views.add, name='add'),
    path('mainmenu/', views.mainmenu, name='mainmenu'),
    path('delete/', views.delete, name='delete')
]
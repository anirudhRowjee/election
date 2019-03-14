from django.urls import path, include
from . import views

urlpatterns = [
    #path('', views.home, name='home'),
    path('all/', views.view_all, name='view_all_candidates'),
    path('add/', views.add, name='add_candidates'),
    path('mainmenu/', views.mainmenu, name='mainmenu_candidates'),
    path('delete/', views.delete, name='delete_candidates')
]
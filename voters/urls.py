from django.urls import path, include
from . import views

urlpatterns = [
    path('view/', views.view_voters, name='view_voters'),
    path('populate/', views.populate_voters, name='populate_voters'),
    path('delete/', views.delete_voters, name='delete_voters'),
    path('mainmenu/', views.main_menu, name='mainmenu_voters'),
]

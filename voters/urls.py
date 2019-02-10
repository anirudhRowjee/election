from django.urls import path, include
from . import views

urlpatterns = [
    path('view/', views.view_voters, name='view'),
    path('populate/', views.populate_voters, name='populate'),
    path('delete/', views.delete_voters, name='delete_v'),
    path('mainmenu/', views.main_menu, name='mainmenu'),
]

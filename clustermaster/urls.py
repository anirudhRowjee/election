from django.urls import include, path
from . import views


urlpatterns = [
    path('clusters/', views.clustermaster, name='clustermaster_mainmenu'),
    path('add/', views.add_cluster, name='add_cluster'),
]
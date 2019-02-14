from django.urls import include, path
from . import views


urlpatterns = [
    path('clusters/', views.clustermaster, name='clustermaster_mainmenu'),
    path('add/', views.add_cluster, name='add_cluster'),
    path('deletecluster/<int:cluster_id>/', views.delete_cluster, name='delete_cluster'),
    path('togglecluster/<int:cluster_id>/<int:status>/', views.control_cluster, name='togglecluster'),
]
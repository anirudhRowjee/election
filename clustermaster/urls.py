from django.urls import include, path
from . import views

cluster_urls = [
    path('create/', views.add_cluster, name='create_cluster'),
    path('mainmenu/', views.cluster_mainmenu, name='cluster_mainmenu'),
    path('remove/', views.delete_cluster, name='delete_cluster'),
]

booth_urls = [
    path('control/<int:booth_id>/', views.control_booth, name='control_booth'),
    path('history/<int:booth_id>/', views.show_history_booth, name='booth_history'),
    path('mainmenu/', views.booth_mainmenu, name='booth_mainmenu')
]

urlpatterns = [
    path('mainmenu/', views.mainmenu, name='clustermaster_mainmenu'),
    path('clusters/', include(cluster_urls), name='cluster_urls'),
    path('booths/', include(booth_urls), name='booths_urls'),
]
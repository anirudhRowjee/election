from django.urls import path, include
from . import views

election_urls = [
    path('home/', views.home_elections, name='home_election'),
    path('create/', views.create_elections, name='create_election'),
    path('activate/', views.activate_elections, name='activate_election'),
    path('declare/', views.declare_elections, name='declare_election'),
    path('reset/', views.reset_elections, name='reset_election'),
    path('all/', views.all_elections, name='all_election'),
    path('live/', views.live_results, name='live_results')
]

posts_urls = [
    path('create/', views.create_posts, name='create_post'),
    path('home/', views.home_posts, name='home_post'),
    path('remove/', views.remove_posts, name='remove_post'),
    path('all/', views.all_posts, name='all_post'),
]

votertypes_urls = [
    path('create/', views.create_votertype, name='create_votertype'),
    path('home/', views.home_votertype, name='home_votertype'),
    path('remove/', views.remove_votertype, name='remove_votertype'),
    path('all/', views.all_votertype, name='all_votertypes'),
]

urlpatterns = [
    path('mainmenu/', views.home, name='menu'),
    path('election_ops/', include(election_urls), name='admin'),
    path('posts/', include(posts_urls), name='posts'),
    path('votertypes/', include(votertypes_urls), name='votertypes'),
]

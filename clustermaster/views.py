from django.shortcuts import render
from clustermaster import models
# Create your views here.


def mainmenu(request):
    return render(request, 'clustermaster/mainmenu.html')

# Cluster management

def cluster_mainmenu(request):
    pass

def add_cluster(request):
    pass

def delete_cluster(request):
    pass

def activate_cluster(request):
    pass

def deactivate_cluster(request):
    pass

# Booth Management

def create_booth(request):
    pass

def delete_booth(request):
    pass

def control_booth(request):
    pass

def show_history_booth(request):
    pass

def send_voter_to_booth(request):
    pass
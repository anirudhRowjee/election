from django.shortcuts import render
from clustermaster import models as cl_models
from elections import models as e_models
# Create your views here.
from uuid import uuid4 as pwd
from . import forms

def clustermaster(request):
    if request.method == 'POST':
        pass
    else:
        clusters = cl_models.Cluster.objects
        elections = e_models.Election.objects
        return render(request, 'clustermaster/mainmenu.html', {'clusters': clusters, 'elections': elections})


def add_cluster(request):
    if request.method == 'POST':
        form = forms.AddCluster(request.POST)

    else:
        form = forms.AddCluster()
        return render(request, 'clustermaster/cluster/create.html', {'form':form})

# Cluster management





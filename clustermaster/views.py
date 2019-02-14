from django.shortcuts import render
from clustermaster import models as cl_models
from elections import models as e_models
# Create your views here.
import uuid as pwd
from . import forms, urls
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


@login_required()
def clustermaster(request):
    if request.method == 'POST':
        pass
    else:
        clusters = cl_models.Cluster.objects
        elections = e_models.Election.objects
        return render(request, 'clustermaster/mainmenu.html', {'clusters': clusters, 'elections': elections})

@login_required()
def add_cluster(request):
    if request.method == 'POST':
        form = forms.AddCluster(request.POST)
        if form.is_valid():
            cluster = form.save(commit=False)
            cluster.password = pwd.uuid4().hex.upper()[0:6]
            try:
                cluster.save()
                cluster.username = 'cluster_' + str(cluster.id)
                cluster.save()
            except IntegrityError:
                return render(request, 'clustermaster/mainmenu.html', {'error':'This cluster Already Exists'})
            clusters = cl_models.Cluster.objects
            elections = e_models.Election.objects
            return render(request, 'clustermaster/has_been_created.html', {'item':cluster})
        else:
            pass
    else:
        form = forms.AddCluster()
        return render(request, 'clustermaster/cluster/create.html', {'form':form})

# Cluster management

@login_required()
def delete_cluster(request, cluster_id='None'):
    cluster_tbd = cl_models.Cluster.objects.get(id=cluster_id)
    cluster_tbd.delete()
    clusters = cl_models.Cluster.objects
    elections = e_models.Election.objects
    return render(request, 'clustermaster/has_been_deleted.html' , {'object':cluster_id})


@login_required()
def control_cluster(request, cluster_id='None', status=0):
    cluster_tbc = cl_models.Cluster.objects.get(id=cluster_id)
    if int(status) == 0:
        cluster_tbc.status = False
        cluster_tbc.save()
        return render(request, 'clustermaster/has_been_changed.html', {'id': id})
    elif int(status) == 1:
        cluster_tbc.status = True
        cluster_tbc.save()
        return render(request, 'clustermaster/has_been_changed.html', {'id': id})






from django.shortcuts import render
# Create your views here.
from clustermaster import models as cl_models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group


def home(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.groups.filter(name='Clusters').exists():
                parent_cluster = cl_models.Cluster.objects.get(username=request.POST['username'])
                booths = cl_models.Booth.objects.all().filter(cluster=parent_cluster)
                return render(request, 'votes/director.html', {'cluster':parent_cluster, 'booths':booths, 'user':user, 'type':'c'})
            elif user.groups.filter(name='Booths').exists():
                booth = cl_models.Booth.objects.get(username=request.POST['username'])
                return render(request, 'votes/director.html', {'booth':booth, 'user':user, 'type':'v'})
            else:
                return render(request, 'votes/home.html', {'error': 'You do not have permission to access this page.'})
        else:
            return render(request, 'votes/home.html', {'error': 'Incorrect Username/Password'})
    else:
        return render(request, 'votes/home.html')

@login_required()
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'logged_out.html')


def cluster(request, cluster_id='None'):
    cluster_o = cl_models.Cluster.objects.get(id=cluster_id)
    booths = cl_models.Booth.objects.all().filter(cluster=cluster_o)
    return render(request, 'votes/cluster.html', {'cluster':cluster_o, 'booths':booths})


def vote(request, booth_id='None'):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'votes/vote.html', {'booth': booth_o, 'user': user_o})


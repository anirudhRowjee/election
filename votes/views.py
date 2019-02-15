from django.shortcuts import render
# Create your views here.
from clustermaster import models as cl_models
from elections import models as e_models
from voters import models as voter_models
from candidates import models as c_models
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
                auth.login(request, user)
                return render(request, 'votes/director.html', {'cluster':parent_cluster, 'booths':booths, 'user':user, 'type':'c'})
            elif user.groups.filter(name='Booths').exists():
                booth = cl_models.Booth.objects.get(username=request.POST['username'])
                auth.login(request, user)
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

@login_required()
def cluster(request, cluster_id='None'):
    cluster_o = cl_models.Cluster.objects.get(id=cluster_id)
    booths = cl_models.Booth.objects.all().filter(cluster=cluster_o)
    return render(request, 'votes/cluster.html', {'cluster':cluster_o, 'booths':booths})


def vote(request, booth_id='None'):
    if request.method == 'POST':
        pass
    else:
        booth = cl_models.Booth.objects.get(id=booth_id)
        cluster = booth.cluster
        election = cluster.election
        candidates = c_models.Candidate.objects.all().filter(election=election)
        posts = e_models.Posts.objects.all()

        candidate_dict = {}
        for post in posts:
            if post not in candidate_dict:
                candidate_dict[post] = []
        for post in candidate_dict:
            candidate_dict[post] = c_models.Candidate.objects.all().filter(post=post)

        return render(request, 'votes/vote.html', {'booth': booth, 'candidates':candidates, 'posts':posts, 'candidate_dict': candidate_dict})


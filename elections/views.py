from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elections import models as e_models
from .forms import *
from django.contrib import auth
from django.db import IntegrityError
# Create your views here.


@login_required()
def home(request):
    return render(request, 'mainmenu/mainmenu.html')

# view functions for elections  sub-app


def home_elections(request):
    return render(request, 'elections/home.html')


def create_elections(request):
    if request.method == 'POST':
        f = AddElection(request.POST)
        if f.is_valid():
            try:
                f.save()
            except IntegrityError as e:
                form = AddElection()
                return render(request, 'elections/create.html', {'form':form, 'error': 'Duplicate Data'})
            elections = e_models.Election.objects
            return render(request, 'elections/all.html', {'elections':elections})
        else:
            form = AddElection()
            return render(request, 'elections/create.html', {'form': form, 'error':'data did not validate'})
    else:
        form = AddElection()
        return render(request, 'elections/create.html', {'form':form})


def activate_elections(request):
    if request.method == 'POST':

        uname = request.POST['superuser_username']
        p1 = request.POST['superuser_password_1']
        p2 = request.POST['superuser_password_2']
        if p1 == p2:
            if auth.authenticate(request, username=uname, password=p1) is not None:
                election_id = request.POST['election_id']
                election_tba = e_models.Election.objects.get(id=election_id)
                election_tba.is_active = True
                election_tba.save()
                elections = e_models.Election.objects
                return render(request, 'elections/all.html', {'elections':elections})
            else:
                posts = e_models.Posts.objects
                return render(request, 'posts/delete.html',
                              {'error': 'WRONG USERNAME/PASSWORD', 'posts': posts})
    else:
        elections = e_models.Election.objects.filter(is_active=False)
        return render(request, 'elections/activate.html', {'elections': elections})


def declare_elections(request):
    pass


def reset_elections(request):
    pass


def all_elections(request):
    elections = e_models.Election.objects
    return render(request, 'elections/all.html', {'elections':elections})


# view functions for sub-app posts


def create_posts(request):
    if request.method == 'POST':
        form = AddNewPost(request.POST)
        post_name = request.POST['post_name']
        post_description = request.POST['post_description']
        e_models.Posts.objects.get_or_create(
            name=post_name,
            description=post_description,
        )
        posts = e_models.Posts.objects
        return render(request, 'posts/all.html', {'posts': posts})
    else:
        form = AddNewPost()
        return render(request, 'posts/create.html', {'form': form})


def home_posts(request):
    return render(request, 'posts/home.html')


def remove_posts(request):
    if request.method == 'POST':
        uname = request.POST['superuser_username']
        p1 = request.POST['superuser_password_1']
        p2 = request.POST['superuser_password_2']
        if p1 == p2:
            if auth.authenticate(request, username=uname, password=p1) is not None:
                post_id = int(request.POST['post_tbd'])
                post_tbd = e_models.Posts.objects.get(id=post_id)
                post_tbd.delete()
                posts = e_models.Posts.objects
                return render(request, 'posts/all.html', {'posts': posts})
            else:
                posts = e_models.Posts.objects
                return render(request, 'posts/delete.html',
                              {'error': 'WRONG USERNAME/PASSWORD', 'posts': posts})
    else:
        posts = e_models.Posts.objects
        return render(request, 'posts/delete.html', {'posts':posts})


def all_posts(request):
    posts = e_models.Posts.objects
    return render(request, 'posts/all.html', {'posts':posts})


# view functions for sub-app voter types

def create_votertype(request):
    if request.method=='POST':
        form = AddNewVotertype(request.POST)
        votertypename = request.POST['votertype_name']
        votertypevalue = request.POST['votertype_votevalue']
        e_models.VoterTypes.objects.get_or_create(
            name=votertypename,
            value=votertypevalue,
        )
        votertypes= e_models.VoterTypes.objects
        return render(request, 'votertypes/all.html', {'votertypes':votertypes})
    else:
        form = AddNewVotertype()
        return render(request, 'votertypes/create.html', {'form':form})


def home_votertype(request):
    return render(request, 'votertypes/home.html')


def remove_votertype(request):
    if request.method == 'POST':
        uname = request.POST['superuser_username']
        p1 = request.POST['superuser_password_1']
        p2 = request.POST['superuser_password_2']
        if p1 == p2:
            if auth.authenticate(request, username=uname, password=p1) is not None:
                votertype_id = int(request.POST['votertype_tbd'])
                votertype_tbd = e_models.VoterTypes.objects.get(id=votertype_id)
                votertype_tbd.delete()
                votertypes = e_models.VoterTypes.objects
                return render(request, 'votertypes/all.html', {'votertypes': votertypes})
            else:
                votertypes = e_models.VoterTypes.objects
                return render(request, 'votertypes/delete.html', {'error': 'WRONG USERNAME/PASSWORD', 'votertypes': votertypes})
        else:
            votertypes = e_models.VoterTypes.objects
            return render(request, 'votertypes/delete.html',
                          {'error': 'PASSWORDS DO NOT MATCH', 'votertypes': votertypes})
    else:
        votertypes = e_models.VoterTypes.objects
        return render(request, 'votertypes/delete.html', {'votertypes':votertypes})


def all_votertype(request):
    votertypes = e_models.VoterTypes.objects
    return render(request, 'votertypes/all.html', {'votertypes':votertypes})


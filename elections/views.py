from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elections import models as e_models

# Create your views here.


@login_required()
def home(request):
    return render(request, 'mainmenu/mainmenu.html')

# view functions for elections  sub-app


def home_elections(request):
    return render(request, 'elections/home.html')


def create_elections(request):
    pass


def activate_elections(request):
    pass


def declare_elections(request):
    pass


def reset_elections(request):
    pass


def all_elections(request):
    elections = e_models.Election.objects
    return render(request, 'elections/all.html', {'elections':elections})


# view functions for sub-app posts


def create_posts(request):
    pass


def home_posts(request):
    return render(request, 'posts/home.html')


def remove_posts(request):
    pass


def all_posts(request):
    posts = e_models.Posts.objects
    return render(request, 'posts/all.html', {'posts':posts})


# view functions for sub-app voter types

def create_votertype(request):
    if request.method=='POST':
        pass
    else:
        return render(request, 'votertypes/add.html')


def home_votertype(request):
    return render(request, 'votertypes/home.html')


def remove_votertype(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'votertypes/delete.html')


def all_votertype(request):
    votertypes = e_models.VoterTypes.objects
    return render(request, 'votertypes/all.html', {'votertypes':votertypes})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required()
def home(request):
    return render(request, 'mainmenu/mainmenu.html')


def home_elections(request):
    return render(request, 'elections/all.html')


def create_elections(request):
    pass


def activate_elections(request):
    pass


def declare_elections(request):
    pass


def reset_elections(request):
    pass


def all_elections(request):
    pass


def create_posts(request):
    pass


def home_posts(request):
    pass


def remove_posts(request):
    pass


def all_posts(request):
    pass


def create_votertype(request):
    pass


def home_votertype(request):
    pass


def remove_votertype(request):
    pass


def all_votertype(request):
    pass


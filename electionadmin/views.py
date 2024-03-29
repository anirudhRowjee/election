# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.shortcuts import redirect
from voters.models import Voters
import voters.views
from elections.models import VoterTypes, VoterLists
from django.contrib.auth.decorators import login_required
import csv
from datetime import datetime
from django.contrib.auth.models import User, Group
from clustermaster import models as c_models


def is_admin(user):
    superusers = Group.objects.get(name="Superusers").user_set.all()
    # print("superusers ", superusers)
    if user in superusers:
        return True
    else:
        return False

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home_electionadmin')
        else:
            return render(request, 'electionadmin/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'electionadmin/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return render(request, 'electionadmin/logged_out.html')


@login_required()
def home(request):
    if is_admin(request.user):
        return render(request, 'electionadmin/home.html')
    else:
        username_meta = request.user.username.split('_')
        if len(username_meta) == 2:
            group = username_meta[0]
            identifier = username_meta[1]
        if len(username_meta) == 4:
            group = 'vote'
            username = request.user.username
            booth = c_models.Booth.objects.get(username=username)
            identifier = booth.id
        return render(request, 'votes/home.html', {'message': 'You do not have access to this page', 'group':group,
                                                   'identifier':identifier})


@login_required(login_url='electionadmin/login.html')
def populate_voters(request):
    if request.method == 'POST':
        if request.POST['voters'].count == 0:
            time_of_creation = datetime.now()
            new = VoterLists(
                filename=str(request.FILES['csv_source'])+str(time_of_creation),
                file=request.FILES['csv_source'],
            )
            new.save()
            file_id = VoterLists.objects.get(filename=str(request.FILES['csv_source'])+str(time_of_creation)).id
            f = VoterLists.objects.get(id=file_id).file.path
            with open(f) as foo:
                reader = csv.reader(foo, delimiter=',')
                for row in reader:
                    Voters.objects.get_or_create(
                        voter_id=str(row[0]).lstrip().rstrip(),
                        name=str(row[1]).lstrip().rstrip(),
                        voter_class=str(row[2]).lstrip().rstrip(),
                        type=VoterTypes.objects.get(id=request.POST['type']),
                    )
            votertypes = VoterTypes.objects
            voters = Voters.objects
            return render(request, 'electionadmin/voters_viewvoters.html', {'votertypes': votertypes, 'voters': voters})
        else:
            votertypes = VoterTypes.objects
            voters = Voters.objects
            return render(request, 'electionadmin/voters_viewvoters.html', {'votertypes': votertypes, 'voters': voters})
    else:
        votertypes = VoterTypes.objects
        voters = Voters.objects
        return redirect(request, 'electionadmin/voter_populate.html', {'votertypes':votertypes, 'voters':voters})


@login_required(login_url='electionadmin/login.html')
def view_voters(request):
    votertypes = VoterTypes.objects
    voters = Voters.objects
    if request.method == 'GET' and request.POST['voters'].count != 0:
        return render(request, 'electionadmin/voters_viewvoters.html', {'votertypes': votertypes, 'voters': voters})
    else:
        return redirect(request, 'electionadmin/voter_populate.html', {'votertypes': votertypes, 'voters': voters})


@login_required(login_url='electionadmin/login.html')
def delete_voters(request):
    pass

# Create your views here.
from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.shortcuts import redirect
from voters.models import Voters
from elections.models import VoterTypes, VoterLists
from django.contrib.auth.decorators import login_required
import csv
from datetime import datetime


# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'electionadmin/login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'electionadmin/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def home(request):
    return render(request, 'electionadmin/home.html')


@login_required(login_url='electionadmin/login.html')
def populate_voters(request):
    if request.method == 'POST':
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
        voters = Voters.objects
        return render(request, 'electionadmin/voter_ops.html', {'votertypes': votertypes, 'voters': voters})
    else:
        votertypes = VoterTypes.objects
        voters = Voters.objects
        return render(request, 'electionadmin/voter_ops.html', {'votertypes':votertypes, 'voters':voters})


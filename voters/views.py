from django.shortcuts import render, HttpResponse
from django.contrib import auth
from django.shortcuts import redirect
from voters.models import Voters
from elections.models import VoterTypes, VoterLists
from django.contrib.auth.decorators import login_required
import csv
from datetime import datetime
# Create your views here.

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
        votertypes = VoterTypes.objects
        voters = Voters.objects
        return render(request, 'voters_admin/view.html', {'votertypes': votertypes, 'voters': voters})
    else:
        votertypes = VoterTypes.objects
        voters = Voters.objects
        return render(request, 'voters_admin/populate.html', {'votertypes': votertypes, 'voters': voters})


@login_required(login_url='electionadmin/login.html')
def view_voters(request):
    votertypes = VoterTypes.objects
    voters = Voters.objects
    if request.method == 'GET':
        return render(request, 'voters_admin/view.html', {'votertypes': votertypes, 'voters': voters})


@login_required(login_url='electionadmin/login.html')
def delete_voters(request):
    if request.method == 'POST':
        uname = request.POST['superuser_username']
        p1 = request.POST['superuser_password_1']
        p2 = request.POST['superuser_password_2']
        if p1 == p2:
            if auth.authenticate(request, username = uname, password=p1) is not None:
                Voters.objects.all().delete()
                votertypes = VoterTypes.objects
                voters = Voters.objects
                return render(request, 'voters_admin/view.html',
                              {'votertypes': votertypes, 'voters': voters, 'error': 'please populate', })
            else:
                votertypes = VoterTypes.objects
                voters = Voters.objects
                return render(request, 'voters_admin/delete.html',
                              {'votertypes': votertypes, 'voters': voters, 'error': 'wrong username or password', })

        else:
            votertypes = VoterTypes.objects
            voters = Voters.objects
            return render(request, 'voters_admin/delete.html', {'votertypes': votertypes, 'voters': voters, 'error': 'passwords do not match',})
    else:
        votertypes = VoterTypes.objects
        voters = Voters.objects
        return render(request, 'voters_admin/delete.html', {'votertypes': votertypes, 'voters': voters})


@login_required()
def main_menu(request):
    return render(request, 'voters_admin/mainmenu.html')

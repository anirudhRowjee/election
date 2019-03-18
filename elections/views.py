from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from elections import models as e_models
from .forms import *
from django.contrib import auth
from django.http import HttpResponse
from django.views.generic import View
from election.utils import render_to_pdf

# Create your views here.
from candidates import models as c_models
from voters import models as v_models

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
            f.save()
            form = AddElection()
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


def reset_elections(request):
    if request.method == 'POST':
        uname = request.POST['superuser_username']
        p1 = request.POST['superuser_password_1']
        p2 = request.POST['superuser_password_2']
        if p1 == p2:
            if auth.authenticate(request, username=uname, password=p1) is not None:
                election_id = request.POST['election_id']
                election_tba = e_models.Election.objects.get(id=election_id)
                # make election is active status = False
                voters = v_models.Voters.objects.all()
                # make all voters has voted status to false
                voters.has_voted = False
                # clear votes data
                vote_models.Vote.objects.all().filter(election=election_tba).delete()
                # clear candidate data
                candidates = c_models.Candidate.objects.all()
                for candidate in candidates:
                    if candidate.election == election_tba:
                        candidate.votes = 0

                voters.save()
                election_tba.save()
                candidates.save()

                elections = e_models.Election.objects
                return render(request, 'elections/all.html', {'error': 'ELECTION HAS BEEN RESET','elections': elections})
            else:
                posts = e_models.Posts.objects
                return render(request, 'posts/delete.html',{'error': 'WRONG USERNAME/PASSWORD', 'posts': posts})
    else:
        elections = e_models.Election.objects
        return render(request, 'elections/reset.html', {'elections':elections})


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


class GeneratePdf(View):
    def get(self, request, data, *args, **kwargs):
        pdf = render_to_pdf('pdf/results.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


def live_results(request):
    if request.method == 'POST':
        election_id = request.POST['election']
        election = e_models.Election.objects.get(id=election_id)
        candidates = c_models.Candidate.objects.all().filter(election=election).order_by('-votes')
        posts = e_models.Posts.objects.all()
        return render(request, 'elections/live.html', {'chosenelection': election, 'candidates':candidates, 'posts':posts,})
    else:
        elections = e_models.Election.objects
        return render(request, 'elections/live.html', {'elections':elections, 'chosenelection':None})


def declare_elections(request):
    if request.method == 'POST':
        uname = request.POST['superuser_username']
        p1 = request.POST['superuser_password_1']
        p2 = request.POST['superuser_password_2']
        election_id = request.POST['election_id']
        election = e_models.Election.objects.get(id=election_id)
        candidates = c_models.Candidate.objects.all().order_by('-votes')
        if p1 == p2:
            if auth.authenticate(request, username=uname, password=p1) is not None:
                # all auth passed
                # generate winners list
                winners = []
                # find candidate with highest votes for every post
                for post in e_models.Posts.objects.all():
                    post_clist = []
                    for candidate in candidates.filter(post=post).order_by('-votes').values('id'):
                        #print(candidate['id'])
                        post_clist.append(candidate['id'])
                    if len(post_clist) == 0:
                        pass
                    else:
                        #print('post_clist', post_clist)
                        winner_id = post_clist[0]
                        winner = c_models.Candidate.objects.get(id=winner_id)
                        winners.append(winner)
                # add pdf file of results
                posts = e_models.Posts.objects.all()
                voter_turnout = v_models.Voters.objects.all().filter(has_voted=True).count()
                voter_total = v_models.Voters.objects.all().count()
                posts_contested = e_models.Posts.objects.all().count()
                election = e_models.Election.objects.get(id=election_id)
                election.is_active = False
                election.save()
                dec_string = "results of election " + str(election.pretty_name) + " Have been declared! "
                data = {'error': dec_string, 'election': election, 'winners': winners,
                                                            'posts': posts, 'candidates':candidates,
                                                            'voter_turnout': voter_turnout, 'voter_total': voter_total,
                                                            'posts_contested': posts_contested}
                return GeneratePdf.get(self=GeneratePdf(), request=request, data=data)
            else:
                elections = e_models.Election.objects
                return render(request, 'elections/declare.html',
                              {'error': 'WRONG USERNAME/PASSWORD', 'elections': elections})
        else:
            elections = e_models.Election.objects
            return render(request, 'elections/declare.html',
                          {'error': 'PASSWORDS DO NOT MATCH', 'elections': elections})
    else:
        elections = e_models.Election.objects.filter(is_active=True)
        return render(request, 'elections/declare.html', {'elections':elections})

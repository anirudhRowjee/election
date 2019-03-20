from django.shortcuts import render
# Create your views here.
from clustermaster import models as cl_models
from elections import models as e_models
from voters import models as voter_models
from candidates import models as c_models
from . import models as vote_models
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.utils.datastructures import MultiValueDictKeyError


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
    if request.method == 'POST':
        voter_id = request.POST['voter_id'].lstrip().rstrip()
        cluster_id = request.POST['cluster']
        cluster_tbv = cl_models.Cluster.objects.get(id=cluster_id)
        booths = cl_models.Booth.objects.all().filter(cluster=cluster_tbv)

        # Check if submitted voter ID belongs to real voter
        try:
            voter = voter_models.Voters.objects.get(voter_id=voter_id)
        except ObjectDoesNotExist:
            return render(request, 'votes/cluster.html', {'cluster': cluster_tbv, 'booths': booths, 'error':'Invalid Voter ID'})

        # Check if the voter has voted
        if voter.has_voted:
            return render(request, 'votes/cluster.html',
                          {'cluster': cluster_tbv, 'booths': booths, 'error': 'Voter has already voted'})

        # Check if voter has been assigned a booth already
        for booth in booths:
            if booth.assigned_voter is None:
                pass
            elif booth.assigned_voter.voter_id == voter_id:
                return render(request, 'votes/cluster.html',
                              {'cluster': cluster_tbv, 'booths': booths, 'error': 'Voter has already Been Assigned A Booth'})

        booths = cl_models.Booth.objects.all().filter(cluster=cluster_tbv).order_by('id')
        for booth in booths:
            if booth.assigned_voter is None:
                booth.assigned_voter = voter
                booth.save()
                break
        cluster_o = cl_models.Cluster.objects.get(id=cluster_id)
        booths = cl_models.Booth.objects.all().filter(cluster=cluster_o)
        return render(request, 'votes/cluster.html', {'cluster': cluster_o, 'booths': booths})
    else:
        cluster_o = cl_models.Cluster.objects.get(id=cluster_id)
        booths = cl_models.Booth.objects.all().filter(cluster=cluster_o)
        return render(request, 'votes/cluster.html', {'cluster':cluster_o, 'booths':booths})


def vote(request, booth_id='None'):
    if request.method == 'POST':
        booth = cl_models.Booth.objects.get(id=booth_id)
        election = booth.cluster.election
        voter = booth.assigned_voter
        votertype = voter.type
        votes = {}
        posts = e_models.Posts.objects.all()

        # making a dictionary with post as key and chosen candidate as the value
        for post in posts:
            # iterate through posts
            pid = post.id
            # get post ID
            try:
                post_id = request.POST[str(pid)]
                votes[pid] = int(post_id)
            except MultiValueDictKeyError:
                pass
                # check if post ID is part of POST data

                # if yes, add to dictionary
        print(votes)
        for vote in votes:
            postid = vote
            candidateid = votes[vote]
            post = e_models.Posts.objects.get(id=postid)
            candidate = c_models.Candidate.objects.get(id=candidateid)
            vote_tbr = vote_models.Vote.objects.create(
                voter=voter,
                candidate=candidate,
                post=post,
                booth=booth,
                election=election,
                votertype=votertype,
            )
            vote_tbr.save()
            votevalue_id = voter.type.id
            votevalue_type = e_models.VoterTypes.objects.get(id=votevalue_id)
            votevalue = votertype.value
            candidate.votes += int(votevalue)
            candidate.save()
        voter.has_voted = True
        voter.save()
        booth.assigned_voter = None
        booth.save()
        candidates = c_models.Candidate.objects.all().filter(election=election)
        return render(request, 'votes/vote.html', {'booth': booth, 'candidates': candidates, 'posts': posts, 'notify':'Thank you for Voting!'})
    else:
        booth = cl_models.Booth.objects.get(id=booth_id)
	    #booth_meta_list = booth.username.split('_')
        #booth_number = booth_meta_list[3]
        cluster_ic = booth.cluster
        election = cluster_ic.election
        candidates = c_models.Candidate.objects.all().filter(election=election)
        posts = []
        for candidate in candidates:
            if candidate.post not in posts:
                posts.append(candidate.post)
        #posts = e_models.Posts.objects.all()
        return render(request, 'votes/vote.html', {'booth': booth, 'candidates':candidates, 'posts':posts, 'b_no':b_no})





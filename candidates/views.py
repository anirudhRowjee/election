from django.shortcuts import render
from candidates import models as c_models
from django.contrib.auth.decorators import login_required
from voters import models as v_models
from elections import models as e_models
# Create your views here.

candidates = c_models.Candidate.objects


@login_required
def view_all(request):
    return render(request, 'candidates_admin/view_all.html', {'candidates': candidates})


@login_required
def add(request):
    if request.method == 'POST':
        voter_id = request.POST['voter_id']
        post = e_models.Posts.objects.get(id=request.POST['post'])
        election = e_models.Election.objects.get(id=request.POST['election'])
        rest = v_models.Voters.objects.get(voter_id=voter_id)
        name = rest.name
        voter_class = rest.voter_class
        c_models.Candidate.objects.get_or_create(
            name=name,
            post=post,
            election=election,
            image=request.FILES.get('image', False),
            logo=request.FILES.get('logo', False),
            voter_id= v_models.Voters.objects.get(voter_id=voter_id),
            slogan=request.POST.get('slogan', False),
            candidate_class= voter_class,
        )
        return render(request, 'candidates_admin/view_all.html', {'candidates':candidates})

    else:
        voters = v_models.Voters.objects.all()
        posts = e_models.Posts.objects.all()
        elections = e_models.Election.objects.all()
        return render(request, 'candidates_admin/add.html', {'voters':voters, 'posts':posts, 'elections':elections})



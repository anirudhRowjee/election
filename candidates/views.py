from django.shortcuts import render
from candidates import models as c_models
from django.contrib.auth.decorators import login_required
from voters import models as v_models
from elections import models as e_models
from django.contrib import auth
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
        v_models.Voters.objects.get(voter_id=voter_id).is_candidate = 'Y'
        v_models.Voters.objects.get(voter_id=voter_id).save()
        return render(request, 'candidates_admin/view_all.html', {'candidates':candidates})
    else:
        voters = v_models.Voters.objects.filter(is_candidate='N')
        posts = e_models.Posts.objects.all()
        elections = e_models.Election.objects.filter(is_active=False)
        return render(request, 'candidates_admin/add.html', {'voters':voters, 'posts':posts, 'elections':elections})


@login_required()
def mainmenu(request):
    return render(request, 'candidates_admin/mainmenu.html')


@login_required()
def delete(request):
    if request.method == 'POST':
        uname = request.POST['superuser_username']
        p1 = request.POST['superuser_password_1']
        p2 = request.POST['superuser_password_2']
        if p1 == p2:
            if auth.authenticate(request, username=uname, password=p1) is not None:
                candidate_id = int(request.POST['candidate_tbd'])
                print(candidate_id)
                candidate_tbd = c_models.Candidate.objects.get(id=candidate_id)
                print(candidate_tbd.voter_id)
                v_models.Voters.objects.get(name=candidate_tbd.voter_id).is_candidate = 'N'
                v_models.Voters.objects.get(name=candidate_tbd.voter_id).save()
                candidate_tbd.delete()
                return render(request, 'candidates_admin/view_all.html',{'error': 'please populate', 'candidates':candidates})
            else:
                return render(request, 'candidates_admin/view_all.html',{'error': 'WRONG USERNAME/PASSWORD', 'candidates':candidates})
    else:
        return render(request, 'candidates_admin/delete.html', {'candidates':candidates})

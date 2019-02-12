from django.db import models
from elections import models as e_models
from voters import models as v_models
from django import forms

# Create your models here.


class Candidate(models.Model):
    voter_id = models.ForeignKey(v_models.Voters, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    candidate_class = models.CharField(max_length=20)
    post = models.ForeignKey(e_models.Posts, on_delete=models.DO_NOTHING)
    election = models.ForeignKey(e_models.Election, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='media/candidates/images')
    logo = models.ImageField(upload_to='media/candidates/logos')
    slogan = models.CharField(max_length=30)
    votes = models.IntegerField(null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' for ' + str(self.post)

    def pretty_name(self):
        return self.name + ' for ' + str(self.post) + ' in ' + str(self.election)




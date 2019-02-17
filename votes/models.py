from django.db import models
from voters import models as v_models
from clustermaster import models as cl_models
from candidates import models as c_models
from elections import models as e_models
# Create your models here.


class Vote(models.Model):
    voter = models.ForeignKey(v_models.Voters, on_delete=models.DO_NOTHING)
    candidate = models.ForeignKey(c_models.Candidate, on_delete=models.DO_NOTHING)
    post = models.ForeignKey(e_models.Posts, on_delete=models.DO_NOTHING)
    booth = models.ForeignKey(cl_models.Booth, on_delete=models.DO_NOTHING)
    time_of_vote = models.DateTimeField(auto_now=True)
    election = models.ForeignKey(e_models.Election, on_delete=models.DO_NOTHING)
    votertype = models.ForeignKey(e_models.VoterTypes, on_delete=models.DO_NOTHING)
    vote_is_good = models.BooleanField(default=True)

    def __str__(self):
        return str(self.voter.voter_id) + ' has voted for ' + str(self.candidate)

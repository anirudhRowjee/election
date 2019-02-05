from django.db import models
from elections import models as election_models
# Create your models here.


class Voters(models.Model):
    voter_id = models.CharField(max_length=20, blank=True, null=True, unique=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    voter_class = models.CharField(max_length=9, blank=True, null=True)
    type = models.ForeignKey(election_models.VoterTypes, on_delete=models.DO_NOTHING)
    has_voted = models.CharField(max_length=1, default='N')


    class Meta:
        managed = True
        verbose_name_plural = 'voters'

    def __str__(self):
        return self.name

# TODO setup interface for client-side csv database normalization

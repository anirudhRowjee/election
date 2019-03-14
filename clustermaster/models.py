from django.db import models
from voters import models as voter_models
from elections import models as e_models
import elections


class Cluster(models.Model):

    def __str__(self):
        return 'cluster ' + str(self.id)

    capacity = models.IntegerField(default=30)
    status = models.BooleanField(default=False)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    election = models.ForeignKey(e_models.Election, on_delete=models.DO_NOTHING, null=True)


class Booth(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    booth_status = models.BooleanField(default=False)
    assigned_voter = models.ForeignKey(voter_models.Voters, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return 'booth_' + str(self.id)

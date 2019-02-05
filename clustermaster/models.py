from django.db import models
from voters import models as voter_models
import elections
# Create your models here.


def do_nothing():
    pass


class Cluster(models.Model):

    def __str__(self):
        return 'cluster_' + str(self.id)

    def get_username(self):
        return 'cluster_' + str(self.id)

    capacity = models.IntegerField(default=30)
    status = models.BooleanField(default=False)
    username = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=20)
    location = models.CharField(max_length=50)


class Booth(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.DO_NOTHING)
    username = models.CharField(max_length=11, unique=True)
    password = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    #last_voter = models.ForeignKey(voter_models.Voters, on_delete=models.DO_NOTHING, default='unknown')
    status = models.BooleanField(default=False)

    def __str__(self):
        return 'booth_' + str(self.id)

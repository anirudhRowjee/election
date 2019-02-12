from django.db import models
from voters import models as voter_models
import elections
import string, random


def password_generator():
    size = 6
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


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
    booth_status = models.BooleanField(default=False)
    assigned_voter = models.ForeignKey(voter_models.Voters, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return 'booth_' + str(self.id)

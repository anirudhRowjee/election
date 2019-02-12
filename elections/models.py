from django.db import models
import datetime
# Create your models here.


class Election(models.Model):

    current_year = datetime.date.today().year
    now = datetime.datetime.now
    year = models.IntegerField(default=current_year)
    election_number = models.IntegerField(default=1)
    is_active = models.BooleanField(default=False)
    type = models.CharField(default='General Election', max_length=50)
    created_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('year', 'election_number', 'type'),)

    def __str__(self):
        name = self.type + ' ' + str(self.year)
        return name

    def pretty_name(self):
        name = self.type + ' ' + str(self.year) + ' ' + str(self.election_number)
        return name



class Posts(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'posts'


class VoterTypes(models.Model):
    name = models.CharField(max_length=20, unique=True)
    value = models.IntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Voter Types'

    def __str__(self):
        return self.name


class VoterLists(models.Model):
    filename = models.CharField(max_length=100)
    file = models.FileField(upload_to='media/voterlists/')
    voterType = models.ForeignKey
    migrated = models.DateTimeField(auto_now=True)

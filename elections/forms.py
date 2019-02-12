from django import forms
from django.forms import ModelForm
from elections import models

class AddNewVotertype(forms.Form):
    votertype_name = forms.CharField(label='Name of Voter Type', required=True, max_length=20)
    votertype_votevalue = forms.IntegerField(label='Value of 1 Vote', required=True)


class AddNewPost(forms.Form):
    post_name = forms.CharField(label="Name of Post", required=True, max_length=20)
    post_description = forms.CharField(label="Description of post", required=True, max_length=100)


class AddElection(ModelForm):
    class Meta:
        model = models.Election
        fields = ['year', 'election_number', 'type']



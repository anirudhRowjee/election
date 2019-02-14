from django import forms
from . import models


class AddCluster(forms.ModelForm):
    class Meta:
        model = models.Cluster
        fields = ['capacity', 'location', 'username', 'election']

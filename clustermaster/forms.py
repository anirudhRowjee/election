from django import forms

from . import models


class AddCluster(forms.ModelForm):
    class Meta:
        model = models.Cluster
        fields = ['capacity', 'location', 'election']
        widgets = {
            'capacity': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'No. of booths in cluster',
                    'style': "width:100%;height: 10vw;"
                }),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'choose location of cluster',
                    'style': "width:100%;height: 10vw;"
                }),

            'election': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'choose election',
                    'style': "width:100%;height: 10vw;"
                }),

        }


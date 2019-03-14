from django import forms
from django.forms import ModelForm
from django.forms import widgets
from elections import models
from django.utils.translation import gettext_lazy as _

class AddNewVotertype(ModelForm):
    class Meta:
        model = models.VoterTypes
        fields = ('name', 'value',)
        labels = {
            'name': _("Name of Votertype "),
            'description': _('Value'),
        }
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Name of votertype',
                    'style': ""
                }),
            'value': forms.widgets.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Value of votertype',
                    'style': ""
                })
        }


class AddNewPost(ModelForm):
    class Meta:
        model = models.Posts
        fields = ('name','description',)
        labels = {
            'name': _("Name of post "),
            'description': _('Description'),
        }
        widgets = {
            'name': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Name of post',
                    'style': ""
                }),
            'description': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Description of post',
                    'style': ""
                })
        }

class AddElection(ModelForm):
    class Meta:
        model = models.Election
        fields = ('type','year', 'election_number', )
        labels = {
            'year': _("Year"),
            'election_number': _("Election ID"),
            'type': _("Name")
        }
        widgets = {
            'type': forms.widgets.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Name of elections',
                    'style': ""
                }),

            'year': forms.widgets.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'Year of elections',
                    'autocomplete': 'off',
                    'style': ""
                }),
            'election_number': forms.widgets.NumberInput(
                attrs={
                    'class': 'form-control',
                    'required': True,
                    'placeholder': 'ID of election',
                    'style': ""
                }),
        }


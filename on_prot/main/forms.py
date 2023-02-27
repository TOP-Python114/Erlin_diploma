from django import forms
from django.forms import fields, ModelForm
from django.forms import widgets
from .models import AllCompetition, SportsmenRegistration, Armwrestler


class DateInput(forms.DateInput):
    input_type = 'date'


class CompetitionForm(ModelForm):
    class Meta:
        model = AllCompetition
        fields = ["title", "date"]
        widgets = {
            'date': DateInput(),
        }


class SportsmenRegistrationForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.all(), required=True)
    sportsmen = forms.ModelChoiceField(queryset=Armwrestler.objects.all(), required=True)

# class Meta:
    #     model=SportsmenRegistration
    #     fields=["competition",'sportsmen']


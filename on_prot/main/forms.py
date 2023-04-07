from django import forms
from django.forms import fields, ModelForm, TextInput
from django.forms import widgets
from .models import AllCompetition, SportsmenRegistration, Armwrestler, AllResults


class DateInput(forms.DateInput):
    input_type = 'date'





class CompetitionForm(ModelForm):
    class Meta:
        model = AllCompetition
        fields = ["title", "date"]
        widgets = {
            'title':TextInput(attrs={'placeholder': 'Введите название старта','class':'input_c'}),
            'date': DateInput(attrs={'class':'input_c'}),
        }

class NewSportsmenForm(ModelForm):
    class Meta:
        model = Armwrestler
        fields = ["name", "age","weight_category","team","sex","grade"]
        widgets = {
            'name':TextInput(attrs={'placeholder': 'Ф.И.О','class':'input_c'}),
            'age': TextInput(attrs={'placeholder': 'Возраст','class':'input_c'}),
            'weight_category': TextInput(attrs={'placeholder': 'Вес','class': 'input_c'}),
            'team': TextInput(attrs={'placeholder': 'Команда','class': 'input_c'}),
            'sex': TextInput(attrs={'placeholder': 'пол','class': 'input_c'}),
            'grade': TextInput(attrs={'placeholder': 'Квалификация','class': 'input_c'}),

        }


class SportsmenRegistrationForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=False), required=True,empty_label="Выберите соревнование")
    sportsmen = forms.ModelChoiceField(queryset=Armwrestler.objects.all(), required=True,empty_label="Выберите спортсмена для регистрации")
    weight = forms.FloatField(required=True, label="уточните вес",
                                       widget=forms.NumberInput(attrs={'placeholder': 'Уточните вес','class': 'input_c'}))

class CreatingCompetitionForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=False), required=True,empty_label="Выберите соревнование")


class FindCompetitionForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=True), required=True,empty_label="Выберите соревнование")


# class WeightClarification(forms.Form):
#     """класс подтверждение веса"""
#     sportsmen = forms.ModelChoiceField(queryset=Armwrestler.objects.filter


# class Meta:
#     model=SportsmenRegistration
#     fields=["competition",'sportsmen']

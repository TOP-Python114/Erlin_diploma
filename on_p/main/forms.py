from django import forms
from .models import Trainer, Armwrestler, Tournaments


class TrainerForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    team = forms.CharField(max_length=99)
    students = forms.ModelMultipleChoiceField(
        queryset=Armwrestler.objects.all(),

        # widget=forms.SelectMultiple,
    )


class TournamentPreRegistrationForm(forms.Form):
    tournament = forms.ModelChoiceField(
        queryset=Tournaments.objects.all(),
    )
    sportsmen = forms.ModelChoiceField(
        queryset=Armwrestler.objects.all(),
    )
    weight_category = forms.ChoiceField(
        choices=[(x, x) for x in ('60', '65', '70', '75', '80', '85', '90', '100', '110', '+110')],

    )


from django import forms

# BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
# FAVORITE_COLORS_CHOICES = [
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# ]
#
# class SimpleForm(forms.Form):
#    # birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     favorite_colors = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_COLORS_CHOICES,
#     )

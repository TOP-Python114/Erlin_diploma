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



# class ProtocolForm(ModelForm):
#     class Meta:
#         model = AllResults
#         fields = ['sportsmen', 'competition', 'points', 'points_left', 'points_right', 'left_place', 'right_place',
#                   'sum_place']


#
# sportsmen = models.ForeignKey(Armwrestler, on_delete=models.CASCADE)
#     competition = models.ForeignKey(AllCompetition, on_delete=models.CASCADE)
#     points=models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(50)],default=0)
#     points_left=models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(25)],default=0)
#     points_right = models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(25)], default=0)
#     left_place = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=100)
#     right_place = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=100)
#     sum_place= models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=100)


class SportsmenRegistrationForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=False), required=True,empty_label="Выберите соревнование")
    sportsmen = forms.ModelChoiceField(queryset=Armwrestler.objects.all(), required=True,empty_label="Выберите спортсмена для регистрации")


class CreatingCompetitionForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=False), required=True,empty_label="Выберите соревнование")


class FindCompetitionForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=True), required=True,empty_label="Выберите соревнование")

# class Meta:
#     model=SportsmenRegistration
#     fields=["competition",'sportsmen']

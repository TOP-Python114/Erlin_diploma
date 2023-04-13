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
            'title': TextInput(attrs={'placeholder': 'Введите название старта', 'class': 'input_c'}),
            'date': DateInput(attrs={'class': 'input_c'}),
        }


grades = (('б/р', 'Без разряда'),
          ('3юн.', "III юношеский"),
          ('2юн.', "II юношеский"),
          ('1юн.', "I юношеский"),
          ('3взр.', "III взрослый"),
          ('2взр.', "II взрослый"),
          ('1взр', "I взрослый"),
          ('КМС', "КМС"),
          ('МС', "Мастер спорта России"),
          ('МСМК', "Мастер спорта России международного класса"),
          ('ЗМС', "Заслуженный мастер спорта"),
          )


class NewSportsmenForm(ModelForm):
    sex = forms.ChoiceField(widget=forms.Select, choices=(('m', 'мужчина'), ('w', 'женщина')))
    grade = forms.ChoiceField(widget=forms.Select, choices=grades)

    class Meta:
        model = Armwrestler
        fields = ["name", "age", "weight_category", "team", "sex", "grade",'image']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Ф.И.О', 'class': 'input_c'}),
            'age': TextInput(attrs={'placeholder': 'Возраст', 'class': 'input_c'}),
            'weight_category': TextInput(attrs={'placeholder': 'Вес', 'class': 'input_c'}),
            'team': TextInput(attrs={'placeholder': 'Команда', 'class': 'input_c'}),
            # 'sex': TextInput(attrs={'placeholder': 'пол','class': 'input_c'}),
            'grade': TextInput(attrs={'placeholder': 'Квалификация', 'class': 'input_c'}),

        }


class SportsmenRegistrationForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=False), required=True,
                                         empty_label="Выберите соревнование")
    sportsmen = forms.ModelChoiceField(queryset=Armwrestler.objects.all(), required=True,
                                       empty_label="Выберите спортсмена для регистрации")

    weight = forms.FloatField(required=True, label="уточните вес",
                              widget=forms.NumberInput(attrs={'placeholder': 'Уточните вес', 'class': 'input_c'}))


class CreatingCompetitionForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=False), required=True,
                                         empty_label="Выберите соревнование")


class FindCompetitionForm(forms.Form):
    competition = forms.ModelChoiceField(queryset=AllCompetition.objects.filter(done=True), required=True,
                                         empty_label="Выберите соревнование")

# class WeightClarification(forms.Form):
#     """класс подтверждение веса"""
#     sportsmen = forms.ModelChoiceField(queryset=Armwrestler.objects.filter


# class Meta:
#     model=SportsmenRegistration
#     fields=["competition",'sportsmen']

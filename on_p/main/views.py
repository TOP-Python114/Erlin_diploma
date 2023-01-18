from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from .models import Armwrestler,Trainer,TournamentPreRegistrationModel
from .forms import TrainerForm, TournamentPreRegistrationForm


# Create your views here.



def list_of_trainers(request):
    return render(request,'main/trainers.html',{
        "trs": Trainer.objects.all()
    })

def tr_register(request):
    if request.method == 'GET':
        return render(request, 'main/tr_register.html', {
            'form': TrainerForm(),
                      })
    elif request.method=='POST':
        form = TrainerForm(request.POST)

        if form.is_valid():
            ff=form.cleaned_data
            print(ff)
            new_trainer=Trainer(
                first_name=ff["first_name"],
                last_name=ff["last_name"],
                team=ff["team"],
                #students=ff['students']
            )
            new_trainer.save()
            for stud in ff['students']:
                new_trainer.students.add(stud)
                new_trainer.save()

        print(request.path)
        return HttpResponseRedirect(request.path)



def trainers(request,pk:int):
    return render(request, 'main/sportsmens.html', {"trainer": Trainer.objects.get(pk=pk)})

def index(request):
    return render(request, 'main/index.html')



def tournament(request):
    if request.method == 'GET':
        return render(request, 'main/tournament.html', {
            'form_tournament': TournamentPreRegistrationForm()
                      })
    elif request.method=='POST':
        form_tour = TournamentPreRegistrationForm(request.POST)

        if form_tour.is_valid():
            ff=form_tour.cleaned_data
            print(ff)
            new_tournament=TournamentPreRegistrationModel(
                date=ff['tour'],
                sportsmen=ff['sportsmen'],
                weight_category=ff['weight_category'],

            )
            new_tournament.save()

        print(request.path)
        return HttpResponseRedirect(request.path)
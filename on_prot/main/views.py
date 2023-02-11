from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Armwrestler, Competition
from main.comp_n import Competition, Sportsmen


# Create your views here.

def hello(request):
    return render(request, 'index.html')

# def select_category_parcer(category):
#     if



def competition_creating():
    game_start=False
    def list_of_categories(li=Armwrestler.objects.all()):
        """проходит по всем объектам борцов и выдает списком все использующиеся категории"""
        categories = set()
        for i in li:
            if i.weight_category not in categories:
                categories.add(str(i.weight_category))
        return sorted(categories)
    dict_category_sportsmens={}
    #словарь в котором ключ - категория, а значение список спортсменов

    dict_category_competition={}
    #словарь в котором ключ - категория, а значение объект соревнования

    def configure_list_of_sportsmen():
        """делает дикт категория, список объектов спортсмен данного мероприятия"""
        for category in list_of_categories():
            for armwres in Armwrestler.objects.all():
                if str(armwres.weight_category)==category:
                    if category not in dict_category_sportsmens:

                        dict_category_sportsmens[category]=[Sportsmen(armwres.name,armwres.weight_category,armwres.age)]

                    else:
                        dict_category_sportsmens[category]+=[Sportsmen(armwres.name,armwres.weight_category,armwres.age)]
        return dict_category_sportsmens

    configure_list_of_sportsmen()
    for cat,sps in dict_category_sportsmens.items():
        dict_category_competition[cat]=Competition(sps,"left",cat,"кубок британии")

    return dict_category_competition

a=competition_creating()


def competition(request):
    result = list(map(str, a["120"].results)) if len(a["120"].results) == len(a["120"].not_paired_sps) else []
    if request.method == 'POST':
        if a["120"].game_over:
            print("Игра все!!!!!!!!!!!!!!!!!!!!!!!")
            return  render(request, 'competit.html', {"result":{i+1:j for i,j in enumerate(result)} })
        if "winnerisone" in request.POST:
            a["120"].fight(1)

        elif "winneristwo" in request.POST:
            print("Победил второй")
            a["120"].fight(2)

    res_gr_a = a["120"].return_group_a().split('\n')
    res_gr_b = a["120"].return_group_b().split('\n')


    try:
        sp1=a["120"].sportsmen1
        sp2=a["120"].sportsmen2
    except:
        sp1 = a["120"].sportsmen1
        sp2 = a["120"].sportsmen1

    return render(request, 'competit.html', {

        "sps": list(map(str,a["120"].not_paired_sps)),

        # "gr_a":a["120"].group_a[a["120"].tour],
        "resa":res_gr_a,
        "resb": res_gr_b,
        "tour":a["120"].tour,
        "result": {i+1:j for i,j in enumerate(result)},
        "sportsmen1": sp1,
        "sportsmen2": sp2

    })

from pprint import pprint

from django.shortcuts import render
from .models import Armwrestler, Competition
from main.comp_n import Competition, Sportsmen


# Create your views here.

def hello(request):
    return render(request, 'index.html')


def competition(request):

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



    #print(dict_category_sportsmens)







    return render(request, 'competit.html', {
        "arms": list_of_categories()
    })

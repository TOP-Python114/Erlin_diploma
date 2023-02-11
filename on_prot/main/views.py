from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Armwrestler, Competition
from main.comp_n import Competition, Sportsmen


# Create your views here.

def hello(request):
    return render(request, 'index.html')


def select_category_parcer(category, sex):
    """принимает вес и выводит категорию и пол"""
    mens = [110, 100, 90, 90, 85, 80, 75, 70, 65, 60, 55]
    woman = [80, 75, 70, 65, 60, 55, 50]
    if sex == 'm':
        for i in mens:
            if int(category) > 110:
                return "+110"
            if int(category) > i:
                return str(mens[mens.index(i) - 1])
        return mens[-1]
    elif sex == 'w':
        for i in woman:
            if int(category) > 80:
                return "+80"
            if int(category) > i:
                return str(woman[woman.index(i) - 1])
        return woman[-1]


def competition_creating(name_of_competition: str):
    def list_of_categories(li=Armwrestler.objects.all()):
        """проходит по всем объектам борцов и выдает списком все использующиеся категории"""
        categories = set()

        for i in li:
            if select_category_parcer(i.weight_category, 'm') not in categories:
                categories.add(select_category_parcer(i.weight_category, 'm'))

        print(categories)
        return sorted(categories)

    dict_category_sportsmens = {}
    # словарь в котором ключ - категория, а значение список спортсменов

    dict_category_competition = {}

    # словарь в котором ключ - категория, а значение объект соревнования

    def configure_list_of_sportsmen():
        """делает дикт категория, список объектов спортсмен данного мероприятия"""
        for category in list_of_categories():
            for armwres in Armwrestler.objects.all():
                if select_category_parcer(armwres.weight_category,'m') == category:
                    if category not in dict_category_sportsmens:

                        dict_category_sportsmens[category] = [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age)]

                    else:
                        dict_category_sportsmens[category] += [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age)]
        return dict_category_sportsmens

    configure_list_of_sportsmen()
    for cat, sps in dict_category_sportsmens.items():
        dict_category_competition[cat] = Competition(sps, "left", cat, name_of_competition)
    pprint(dict_category_competition)
    return dict_category_competition


a = competition_creating("Кубок залупьей радости")


def competition(request, category):
    result = list(map(str, a[category].results)) if len(a[category].results) == len(a[category].not_paired_sps) else []
    if request.method == 'POST':
        if a[category].game_over:
            print("Игра все!!!!!!!!!!!!!!!!!!!!!!!")
            return render(request, 'competit.html', {"result": {i + 1: j for i, j in enumerate(result)}})
        if "winnerisone" in request.POST:
            a[category].fight(1)

        elif "winneristwo" in request.POST:
            print("Победил второй")
            a[category].fight(2)

    res_gr_a = a[category].return_group_a().split('\n')
    res_gr_b = a[category].return_group_b().split('\n')

    try:
        sp1 = a[category].sportsmen1
        sp2 = a[category].sportsmen2
    except:
        sp1 = a[category].sportsmen1
        sp2 = a[category].sportsmen1

    return render(request, 'competit.html', {

        "sps": list(map(str, a[category].not_paired_sps)),

        # "gr_a":a[category].group_a[a[category].tour],
        "resa": res_gr_a,
        "resb": res_gr_b,
        "tour": a[category].tour,
        "result": {i + 1: j for i, j in enumerate(result)},
        "sportsmen1": sp1,
        "sportsmen2": sp2

    })

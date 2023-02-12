from pprint import pprint

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Armwrestler, Competition
from main.comp_n import Competition, Sportsmen

CATEGORY_NORMALIZER={
    '60w':"Женщины 60кг",
    '110m':"Мужчины 110кг"

}
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
    """
    надо вынести в отдельный модуль, !!!
    создание дикта в котором
    ключ - код турнирной сетки "110lm" например это категория 110, рука левая мужчины
    значение экземаляр соревнования
    """
    def list_of_categories(li=Armwrestler.objects.all()):
        """проходит по всем объектам борцов и выдает списком все использующиеся категории"""
        w_categories = set()
        m_categories = set()
        for i in li:
            if select_category_parcer(i.weight_category, 'm') not in m_categories:
                m_categories.add(select_category_parcer(i.weight_category, 'm') + "ml")
                m_categories.add(select_category_parcer(i.weight_category, 'm') + "mr")

            if select_category_parcer(i.weight_category, 'w') not in w_categories:
                w_categories.add(select_category_parcer(i.weight_category, 'w') + "wl")
                w_categories.add(select_category_parcer(i.weight_category, 'w') + "wr")

        print(f" мужские{m_categories} женские {w_categories}")
        return sorted(m_categories), sorted(w_categories)

    dict_category_sportsmens = {}
    # словарь в котором ключ - категория, а значение список спортсменов

    dict_category_competition = {}

    # словарь в котором ключ - категория, а значение объект соревнования

    def configure_list_of_sportsmen():
        """делает дикт категория, список объектов спортсмен данного мероприятия"""
        #часть формирующая мужскую часть соревнования
        for m_category in list_of_categories()[0]:
            for armwres in Armwrestler.objects.all():
                if select_category_parcer(armwres.weight_category, 'm') == m_category[:-2] and armwres.sex=="m":
                    if m_category not in dict_category_sportsmens:
                        dict_category_sportsmens[m_category] = [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age, armwres.sex, armwres.grade)]
                    else:
                        dict_category_sportsmens[m_category] += [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age, armwres.sex, armwres.grade)]
        # часть формирующая женскую часть соревнования
        for w_category in list_of_categories()[1]:
            for armwres in Armwrestler.objects.all():
                if select_category_parcer(armwres.weight_category, 'w') == w_category[:-2] and armwres.sex=="w":
                    if w_category not in dict_category_sportsmens:
                        dict_category_sportsmens[w_category] = [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age, armwres.sex, armwres.grade)]
                    else:
                        dict_category_sportsmens[w_category] += [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age, armwres.sex, armwres.grade)]



        print(dict_category_sportsmens)
        return dict_category_sportsmens

    configure_list_of_sportsmen()
    for cat, sps in dict_category_sportsmens.items():
        dict_category_competition[cat] = Competition(sps, "left", cat, name_of_competition)
    pprint(dict_category_competition)
    dict_category_competition["title"]=name_of_competition
    return dict_category_competition


a = competition_creating("Чемпионат новосибирской области по АРМРЕСТЛИНГУ, ")


def competition(request, category):

    if category not in [x[:-1] for x in a]:
        return render(request, 'competit.html', {
            'sps_l':"Категория не представлена",
            'no_visible': None,
            'alert': 'block',
        })

    result_l = list(map(str, a[category+"l"].results)) if len(a[category+"l"].results) == len(
       a[category+"l"].not_paired_sps) else []
    result_r = list(map(str, a[category+'r'].results)) if len(a[category+"r"].results) == len(
        a[category+"r"].not_paired_sps) else []

    if request.method == 'POST':
        # if a[category].game_over:
        #     print("Игра все!!!!!!!!!!!!!!!!!!!!!!!")
        #     return render(request, 'competit.html', {"result": {i + 1: j for i, j in enumerate(result)}})
        if "winnerisonel" in request.POST:
            print(request.POST)
            a[category+"l"].fight(1)
        elif "winneristwol" in request.POST:
            print("Победил второй")
            a[category+"l"].fight(2)
        if "winnerisoner" in request.POST:
            print(request.POST)
            a[category+"r"].fight(1)
        elif "winneristwor" in request.POST:
            print("Победил второй")
            a[category+"r"].fight(2)

    res_gr_a_l = a[category+"l"].return_group_a().split('\n')
    res_gr_b_l = a[category+"l"].return_group_b().split('\n')
    sp1_l = a[category+"l"].sportsmen1
    sp2_l = a[category+"l"].sportsmen2

    res_gr_a_r = a[category+"r"].return_group_a().split('\n')
    res_gr_b_r = a[category+"r"].return_group_b().split('\n')
    sp1_r = a[category+"r"].sportsmen1
    sp2_r = a[category+"r"].sportsmen2


    return render(request, 'competit.html', {
        'no_visible': "flex",
        'alert':None,
        "sps_l": list(map(str, a[category+"l"].not_paired_sps)),
        "sps_r": list(map(str, a[category+"r"].not_paired_sps)),
        "title": a["title"],
        "current_category":CATEGORY_NORMALIZER[category],
        # "gr_a":a[category].group_a[a[category].tour],
        "resa_l": res_gr_a_l,
        "resb_l": res_gr_b_l,
        "resa_r": res_gr_a_r,
        "resb_r": res_gr_b_r,
        "result_l": {i + 1: j for i, j in enumerate(result_l)},
        "result_r": {i + 1: j for i, j in enumerate(result_r)},
        "sportsmen1_l": sp1_l,
        "sportsmen2_l": sp2_l,
        "sportsmen1_r": sp1_r,
        "sportsmen2_r": sp2_r,

    })




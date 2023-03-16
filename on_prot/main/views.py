# from pprint import pprint
from datetime import datetime
from .forms import CompetitionForm, SportsmenRegistrationForm, CreatingCompetitionForm
from .competition_former import CATEGORY_NORMALIZER
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .competition_former import competition_creating
from .models import Armwrestler, AllCompetition, SportsmenRegistration, AllResults


# Create your views here.

def hello(request):
    return render(request, 'index.html',
                  {
                      # "is_categories": is_categories,
                      # "title": a["title"]
                  }
                  )


def reg_competition(request):
    if request.method == "GET":
        return render(request, 'reg_comp.html', {"form": CompetitionForm})
    elif request.method=='POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            comp=AllCompetition(**form.cleaned_data)
            comp.save()
    return redirect(request.path)


def reg_sportsmen(request):
    if request.method == "GET":
        return render(request, 'reg_sportsmen.html', {"form": SportsmenRegistrationForm})
    elif request.method=='POST':

        form = SportsmenRegistrationForm(request.POST)
        if form.is_valid():
            if not SportsmenRegistration.objects.filter(**form.cleaned_data):
                sp_n=SportsmenRegistration(**form.cleaned_data)
                sp_n.save()
    return redirect(request.path)

def competition_constructor(request):
    """
    конструктор соревнования:  по зарегистрированному соревнованию делает старт сохраняет всю инфу о старте в глобальную переменную a
    """
    if request.method == "GET":
        return render(request, 'competition_constructor.html', {"form": CreatingCompetitionForm})
    elif request.method=='POST':
        form=CreatingCompetitionForm(request.POST)
        if "CreatingCompetition" in request.POST:
            if form.is_valid():

                current_comp=SportsmenRegistration.objects.filter(competition=form.cleaned_data["competition"])

                global a
                #список спортсменов текущего старта
                curr_sportsmens=[x.sportsmen for x in current_comp]
                if not curr_sportsmens:
                    return render(request, 'competition_constructor.html', {"form": CreatingCompetitionForm})

                a=competition_creating(name_of_competition=current_comp[0].competition.title,date_of_competition=current_comp[0].competition.date,li= curr_sportsmens)
                global is_categories
                is_categories = sorted(
                    set([x[:-1].replace("+", "plus") for x in a.keys() if x != 'title' and x != 'date']))
                print(is_categories)
                print("сверху категории")
    # тут рендерим страничку на основе уже страницы соревнований, но с доступами только к меню
    return render(request, 'competit.html', {
        # 'no_visible': "flex",
        'alert': None,
        'no_visible': None,
        "is_categories": is_categories,
    })



#a = competition_creating("Чемпионат новосибирской области по АРМРЕСТЛИНГУ,", date_of_competition=datetime(2022, 5, 17))

#is_categories = sorted(set([x[:-1].replace("+", "plus") for x in a.keys() if x != 'title' and x != 'date']))

def start_is_end(start:dict):
    """
    в текущем соревновании все отборолись
    """
    print([st for st in start if st not in("title","date")])
    print("сверху проверочка")
    for i in [st for st in start if st not in("title","date")]:
        if not start[i].game_over:
            return False
    return True

def save_start(start:dict):
    """сохранение старта в базу"""
    if start_is_end(start):
        for i in [st for st in start if st not in("title","date")]:
            for place_, sp_n in enumerate(start[i].results):
                # если сетка левой руки прошла, сохранить ее в общую таблицу протоколов

                #короче сли рукожопый обновит страницу когда соревы прошли ,спортсмены опыть запишутся в итоговый протокол, эта строка это исключает
                if AllResults.objects.filter(sportsmen=Armwrestler.objects.get(name=sp_n.name)).filter(hand=i[-1]).filter(place=place_ + 1):
                    return


                sp_n_to_save = AllResults(
                    sportsmen=Armwrestler.objects.get(name=sp_n.name),
                    competition=AllCompetition.objects.get(title=a['title']),
                    hand=i[-1],
                    place=place_ + 1
                )


                sp_n_to_save.save()

def competition(request, category):
    # не представленные категории
    # использвуется только если кто то намеренно наберет в адрестну строку не юзаную категорию
    if category not in [x[:-1] for x in a]:
        print("no_active_" + category)
        return render(request, 'competit.html', {
            'sps_l': "Категория не представлена",
            'no_visible': None,
            'alert': 'block',
            'is_categories': is_categories

        })

    if request.method == 'POST':
        if "winnerisonel" in request.POST:
            a[category + "l"].fight(1)
        elif "winneristwol" in request.POST:
            a[category + "l"].fight(2)
        elif "winnerisoner" in request.POST:
            a[category + "r"].fight(1)
        elif "winneristwor" in request.POST:
            a[category + "r"].fight(2)



    #преобразует список объектов по занятым местам в список строк, если сетка завершилась
    result_l = list(map(str, a[category + "l"].results)) if len(a[category + "l"].results) == len(
        a[category + "l"].not_paired_sps) else []
    result_r = list(map(str, a[category + 'r'].results)) if len(a[category + "r"].results) == len(
        a[category + "r"].not_paired_sps) else []
    save_start(a)
    # if a[category + 'l'].game_over:
    #     for place_, sp_n in enumerate(a[category + 'l'].results):
    #         # если сетка левой руки прошла, сохранить ее в общую таблицу протоколов
    #         sp_n_to_save = AllResults(
    #             sportsmen=Armwrestler.objects.get(name=sp_n.name),
    #             competition=AllCompetition.objects.get(title=a['title']),
    #             hand="left",
    #             place=place_+1
    #         )
    #         sp_n_to_save.save()
    #
    # if a[category + 'r'].game_over:
    #     for place_, sp_n in enumerate(a[category + 'r'].results):
    #         sp_n_to_save = AllResults(
    #             sportsmen=Armwrestler.objects.get(name=sp_n.name),
    #             competition=AllCompetition.objects.get(title=a['title']),
    #             hand="right",
    #             place=place_ + 1)
    #         sp_n_to_save.save()
    """
    завершение всего старта
    """
    if start_is_end(a):
        cmps=AllCompetition.objects.get(title=a["title"])
        cmps.done=True
        cmps.save()
    return render(request, 'competit.html', {
        "competition_end" :start_is_end(a),
        'no_visible': "flex",
        'alert': None,
        "sps_l": a[category + "l"].not_paired_sps,
        "sps_r": a[category + "r"].not_paired_sps,
        "title": a["title"],
        "current_category": CATEGORY_NORMALIZER[category],
        "resa_l": a[category + "l"].return_group_a().split('\n'), #группа а левая рука в списке
        "resb_l": a[category + "l"].return_group_b().split('\n'), #группа b левая рука в списке
        "resa_r": a[category + "r"].return_group_a().split('\n'), #группа а правая рука в списке
        "resb_r":  a[category + "r"].return_group_b().split('\n'), #группа b правая рука в списке
        "resfin_l": a[category + "l"].return_final().split('\n'), #финальная группа левая рука
        "resfin_r": a[category + "r"].return_final().split('\n'), #финальная группа правая рука
        "result_l": {i + 1: j for i, j in enumerate(result_l)}, #результаты левая
        "result_r": {i + 1: j for i, j in enumerate(result_r)}, #результаты правая
        "sportsmen1_l": a[category + "l"].sportsmen1, #текущий спортсмен 1 левой руки
        "sportsmen2_l": a[category + "l"].sportsmen2, #текущий спортсмен 2 левой руки
        "sportsmen1_r": a[category + "r"].sportsmen1, #текущий спортсмен 1 правой руки
        "sportsmen2_r": a[category + "r"].sportsmen2, #текущий спортсмен 2 правой руки
        "is_categories": is_categories,
        'rr': '555',
        'game_over_left': a[category + "l"].game_over * "None",
        'game_over_right': a[category + "r"].game_over * "None",
        # видимость надписи результаты соревнований
        'res_left_vis': (not a[category + "l"].game_over) * "None" or 'block',
        'res_right_vis': (not a[category + "r"].game_over) * "None" or 'block',
    })

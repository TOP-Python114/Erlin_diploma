# from pprint import pprint
from datetime import datetime
from .forms import CompetitionForm, SportsmenRegistrationForm, CreatingCompetitionForm
from .competition_former import CATEGORY_NORMALIZER
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .competition_former import competition_creating
from .models import AllResults, Armwrestler,AllCompetition,SportsmenRegistration


# Create your views here.

def hello(request):
    return render(request, 'index.html',
                  {
                      "is_categories": is_categories,
                      "title": a["title"]
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
            sp_n=SportsmenRegistration(**form.cleaned_data)
            sp_n.save()
    return redirect(request.path)

def competition_constructor(request):
    """
    конструктор соревнования
    """
    if request.method == "GET":
        return render(request, 'competition_constructor.html', {"form": CreatingCompetitionForm})
    elif request.method=='POST':
        form=CreatingCompetitionForm(request.POST)
        if "CreatingCompetition" in request.POST:
            if form.is_valid():
                print(form.cleaned_data["competition"])
                current_comp=SportsmenRegistration.objects.filter(competition=form.cleaned_data["competition"])

                for i in current_comp:
                    print(i.sportsmen)
                    print(current_comp[0].competition.date)
                global a
                a=competition_creating(name_of_competition=current_comp[0].competition.title,date_of_competition=current_comp[0].competition.date,li=[x.sportsmen for x in current_comp])
                global is_categories
                is_categories = sorted(
                    set([x[:-1].replace("+", "plus") for x in a.keys() if x != 'title' and x != 'date']))

               #print(SportsmenRegistration.objects.filter(competition=form.cleaned_data["competition"]))
                print("очищеные данные формы")

    #print([x[:-1] for x in a])
    print("конец бублика")

    # if category not in [x[:-1] for x in a]:
    #     print("no_active_" + category)
    #     return render(request, 'competit.html', {
    #         'sps_l': "Категория не представлена",
    #         'no_visible': None,
    #         'alert': 'block',
    #         'is_categories': is_categories
    #
    #     })
    #
    # if request.method == 'POST':
    #
    #     if "winnerisonel" in request.POST:
    #         print(request.POST)
    #         a[category + "l"].fight(1)
    #     elif "winneristwol" in request.POST:
    #         print("Победил второй")
    #         a[category + "l"].fight(2)
    #     elif "winnerisoner" in request.POST:
    #         a[category + "r"].fight(1)
    #     elif "winneristwor" in request.POST:
    #         print("Победил второй")
    #         a[category + "r"].fight(2)
    #
    # res_gr_a_l = a[category + "l"].return_group_a().split('\n')
    # res_gr_b_l = a[category + "l"].return_group_b().split('\n')
    # res_fin_l = a[category + "l"].return_final().split('\n')
    # sp1_l = a[category + "l"].sportsmen1
    # sp2_l = a[category + "l"].sportsmen2
    #
    # res_gr_a_r = a[category + "r"].return_group_a().split('\n')
    # res_gr_b_r = a[category + "r"].return_group_b().split('\n')
    # res_fin_r = a[category + "r"].return_final().split('\n')
    # sp1_r = a[category + "r"].sportsmen1
    # sp2_r = a[category + "r"].sportsmen2
    # result_l = list(map(str, a[category + "l"].results)) if len(a[category + "l"].results) == len(
    #     a[category + "l"].not_paired_sps) else []
    # result_r = list(map(str, a[category + 'r'].results)) if len(a[category + "r"].results) == len(
    #     a[category + "r"].not_paired_sps) else []
    #
    # if a[category + 'l'].game_over:
    #     for place_, sp_n in enumerate(a[category + 'l'].results):
    #         sp_n_to_save = AllResults(
    #             title_competition=a['title'],
    #             date=a['date'],
    #             # надо изменить объекты, чтобы делать распаковку
    #             # sportsmen=Armwrestler(name=sp_n.name,age=sp_n.age,weight_category=sp_n.weight,team=sp_n.team,sex=sp_n.sex,grade=sp_n.grade),
    #             sportsmen=sp_n.name,
    #             category=sp_n.weight,
    #             sex=sp_n.sex,
    #             hand="l",
    #             place=place_ + 1
    #         )
    #         sp_n_to_save.save()
    #
    # if a[category + 'r'].game_over:
    #     for place_, sp_n in enumerate(a[category + 'r'].results):
    #         sp_n_to_save = AllResults(
    #             title_competition=a['title'],
    #             date=a['date'],
    #             # sportsmen=Armwrestler(name=sp_n.name, age=sp_n.age, weight_category=sp_n.weight, team=sp_n.team, sex=sp_n.sex, grade=sp_n.grade),
    #             sportsmen=sp_n.name,
    #             category=sp_n.weight,
    #             sex=sp_n.sex,
    #             hand="r",
    #             place=place_ + 1
    #         )
    #         sp_n_to_save.save()
    #
    # return render(request, 'competit.html', {
    #     'no_visible': "flex",
    #     'alert': None,
    #     "sps_l": a[category + "l"].not_paired_sps,
    #     "sps_r": a[category + "r"].not_paired_sps,
    #     "title": a["title"],
    #     "current_category": CATEGORY_NORMALIZER[category],
    #     "resa_l": res_gr_a_l,
    #     "resb_l": res_gr_b_l,
    #     "resa_r": res_gr_a_r,
    #     "resb_r": res_gr_b_r,
    #     "resfin_l": res_fin_l,
    #     "resfin_r": res_fin_r,
    #     "result_l": {i + 1: j for i, j in enumerate(result_l)},
    #     "result_r": {i + 1: j for i, j in enumerate(result_r)},
    #     "sportsmen1_l": sp1_l,
    #     "sportsmen2_l": sp2_l,
    #     "sportsmen1_r": sp1_r,
    #     "sportsmen2_r": sp2_r,
    #     "is_categories": is_categories,
    #     'rr': '555',
    #     'game_over_left': a[category + "l"].game_over * "None",
    #     'game_over_right': a[category + "r"].game_over * "None",
    #     # видимость надписи результаты соревнований
    #     'res_left_vis': (not a[category + "l"].game_over) * "None" or 'block',
    #     'res_right_vis': (not a[category + "r"].game_over) * "None" or 'block',
    # })
    # redirect("competit.html")
    #return redirect(request.path)
    return render(request, 'competit.html')

# def comp_constructor(request):
#     if request.method == "GET":
#         return render(request, 'competition_constructor.html', {"form": SportsmenRegistrationForm})
#     elif request.method=='POST':
#
#         form = SportsmenRegistrationForm(request.POST)
#         if form.is_valid():
#             sp_n=SportsmenRegistration(**form.cleaned_data)
#             sp_n.save()
#     return redirect(request.path)


# временно




a = competition_creating("Чемпионат новосибирской области по АРМРЕСТЛИНГУ,", date_of_competition=datetime(2022, 5, 17))

is_categories = sorted(set([x[:-1].replace("+", "plus") for x in a.keys() if x != 'title' and x != 'date']))



def competition(request, category,a=a):
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
            print(request.POST)
            a[category + "l"].fight(1)
        elif "winneristwol" in request.POST:
            print("Победил второй")
            a[category + "l"].fight(2)
        elif "winnerisoner" in request.POST:
            a[category + "r"].fight(1)
        elif "winneristwor" in request.POST:
            print("Победил второй")
            a[category + "r"].fight(2)

    res_gr_a_l = a[category + "l"].return_group_a().split('\n')
    res_gr_b_l = a[category + "l"].return_group_b().split('\n')
    res_fin_l = a[category + "l"].return_final().split('\n')
    sp1_l = a[category + "l"].sportsmen1
    sp2_l = a[category + "l"].sportsmen2

    res_gr_a_r = a[category + "r"].return_group_a().split('\n')
    res_gr_b_r = a[category + "r"].return_group_b().split('\n')
    res_fin_r = a[category + "r"].return_final().split('\n')
    sp1_r = a[category + "r"].sportsmen1
    sp2_r = a[category + "r"].sportsmen2
    result_l = list(map(str, a[category + "l"].results)) if len(a[category + "l"].results) == len(
        a[category + "l"].not_paired_sps) else []
    result_r = list(map(str, a[category + 'r'].results)) if len(a[category + "r"].results) == len(
        a[category + "r"].not_paired_sps) else []

    if a[category + 'l'].game_over:
        for place_, sp_n in enumerate(a[category + 'l'].results):
            sp_n_to_save = AllResults(
                title_competition=a['title'],
                date=a['date'],
                # надо изменить объекты, чтобы делать распаковку
                # sportsmen=Armwrestler(name=sp_n.name,age=sp_n.age,weight_category=sp_n.weight,team=sp_n.team,sex=sp_n.sex,grade=sp_n.grade),
                sportsmen=sp_n.name,
                category=sp_n.weight,
                sex=sp_n.sex,
                hand="l",
                place=place_ + 1
            )
            sp_n_to_save.save()

    if a[category + 'r'].game_over:
        for place_, sp_n in enumerate(a[category + 'r'].results):
            sp_n_to_save = AllResults(
                title_competition=a['title'],
                date=a['date'],
                # sportsmen=Armwrestler(name=sp_n.name, age=sp_n.age, weight_category=sp_n.weight, team=sp_n.team, sex=sp_n.sex, grade=sp_n.grade),
                sportsmen=sp_n.name,
                category=sp_n.weight,
                sex=sp_n.sex,
                hand="r",
                place=place_ + 1
            )
            sp_n_to_save.save()

    return render(request, 'competit.html', {
        'no_visible': "flex",
        'alert': None,
        "sps_l": a[category + "l"].not_paired_sps,
        "sps_r": a[category + "r"].not_paired_sps,
        "title": a["title"],
        "current_category": CATEGORY_NORMALIZER[category],
        "resa_l": res_gr_a_l,
        "resb_l": res_gr_b_l,
        "resa_r": res_gr_a_r,
        "resb_r": res_gr_b_r,
        "resfin_l": res_fin_l,
        "resfin_r": res_fin_r,
        "result_l": {i + 1: j for i, j in enumerate(result_l)},
        "result_r": {i + 1: j for i, j in enumerate(result_r)},
        "sportsmen1_l": sp1_l,
        "sportsmen2_l": sp2_l,
        "sportsmen1_r": sp1_r,
        "sportsmen2_r": sp2_r,
        "is_categories": is_categories,
        'rr': '555',
        'game_over_left': a[category + "l"].game_over * "None",
        'game_over_right': a[category + "r"].game_over * "None",
        # видимость надписи результаты соревнований
        'res_left_vis': (not a[category + "l"].game_over) * "None" or 'block',
        'res_right_vis': (not a[category + "r"].game_over) * "None" or 'block',
    })

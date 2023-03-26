# from pprint import pprint
from datetime import datetime
from .forms import CompetitionForm, SportsmenRegistrationForm, CreatingCompetitionForm, \
    FindCompetitionForm,NewSportsmenForm
from .competition_former import CATEGORY_NORMALIZER, select_category_parcer
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .competition_former import competition_creating
from main.models import Armwrestler, AllCompetition, SportsmenRegistration, AllResults


# Create your views here.

def hello(request):
    return render(request, 'index.html',
                  {
                      # "is_categories": is_categories,
                      # "title": a["title"]
                  }
                  )


def protocols(request):
    if request.method == "GET":
        return render(request, 'protocol.html', {"form": FindCompetitionForm,"vis_m":"no_visible","vis_w":"no_visible","vis":"no_visible" })
    if request.method == "POST":
        form = FindCompetitionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data["competition"]
            cat_m_reg = {}
            cat_w_reg = {}
            ikategs = []
            woms=0
            mens=0
            for i in ["55", "60", "65", "70", "75", "80", "85", "90", "100", "110", "+110", ]:
                for j in AllResults.objects.filter(weight_cat=i).filter(competition=data):
                    if j.sportsmen.sex == 'm':
                        mens=1
                        ikategs.append(j)
                ikategs.sort(key=lambda a: a.sum_place)


                if ikategs:
                    cat_m_reg[i] = ikategs
                    ikategs = []
            for i in ["50", "55", "60", "65", "70", "75", "80", "+80"]:
                for j in AllResults.objects.filter(weight_cat=i).filter(competition=data):
                    if j.sportsmen.sex == 'w' :
                        woms=1
                        ikategs.append(j)
                ikategs.sort(key=lambda a: a.sum_place)

                if ikategs:
                    cat_w_reg[i] = ikategs
                    ikategs = []


            req = {"form": FindCompetitionForm,
                   "all_results_m": cat_m_reg,
                   "all_results_w": cat_w_reg,
                   "competition": data.title,
                   "vis_m":"visible"*mens or "no_visible",
                   "vis_w":"visible"*woms or "no_visible",
                   "vis": "visible"
                   }

            return render(request, 'protocol.html', req
                          ,

                          )


def reg_competition(request):
    if request.method == "GET":
        return render(request, 'reg_comp.html', {"form": CompetitionForm})
    elif request.method == 'POST':
        form = CompetitionForm(request.POST)
        if form.is_valid():
            comp = AllCompetition(**form.cleaned_data)
            comp.save()
    return redirect(request.path)

def new_sportsmen(request):
    if request.method == "GET":
        return render(request, 'new_sportsmen.html', {"form": NewSportsmenForm})
    elif request.method == 'POST':
        form = NewSportsmenForm(request.POST)
        if form.is_valid():
            comp = Armwrestler(**form.cleaned_data)
            comp.save()
    return redirect(request.path)




def reg_sportsmen(request):
    if request.method == "GET":
        return render(request, 'reg_sportsmen.html', {"form": SportsmenRegistrationForm})
    elif request.method == 'POST':

        form = SportsmenRegistrationForm(request.POST)
        if form.is_valid():
            if not SportsmenRegistration.objects.filter(**form.cleaned_data):

                sp_n = SportsmenRegistration(**form.cleaned_data)
                sp_n.save()
    return redirect(request.path)


def competition_constructor(request):
    """
    конструктор соревнования:  по зарегистрированному соревнованию делает старт сохраняет всю инфу о старте в глобальную переменную a
    """
    if request.method == "GET":
        return render(request, 'competition_constructor.html', {"form": CreatingCompetitionForm})
    elif request.method == 'POST':
        form = CreatingCompetitionForm(request.POST)
        if "CreatingCompetition" in request.POST:
            if form.is_valid():

                current_comp = SportsmenRegistration.objects.filter(competition=form.cleaned_data["competition"])

                global a
                # список спортсменов текущего старта
                curr_sportsmens = [x.sportsmen for x in current_comp]
                if not curr_sportsmens:
                    return render(request, 'competition_constructor.html', {"form": CreatingCompetitionForm})

                a = competition_creating(name_of_competition=current_comp[0].competition.title,
                                         date_of_competition=current_comp[0].competition.date, li=curr_sportsmens)
                global is_categories
                is_categories = sorted(
                    set([x[:-1].replace("+", "plus") for x in a.keys() if x != 'title' and x != 'date']))

    # тут рендерим страничку на основе уже страницы соревнований, но с доступами только к меню
    return render(request, 'competit.html', {
        # 'no_visible': "flex",
        'alert': None,
        'no_visible': None,
        "is_categories": is_categories,
    })


def start_is_end(start: dict):
    """
    в текущем соревновании все отборолись
    """

    for i in [st for st in start if st not in ("title", "date")]:
        if not start[i].game_over:
            return False
    return True


def sum_place_of_comp(left, right):
    """должен выдать список по суммам рук:
    формат выхода [[объект спортсмена,очки по сумме,очки левая, очки правая,место левая,место правая,место сумма]...]

    """

    res = []
    SCORES = {1: 25, 2: 17, 3: 9, 4: 5, 5: 3, 6: 2}

    for l, r in zip(enumerate(left.results), enumerate(right.results)):

        # нахождение места спортсмена на правую руку
        r2scr = list(map(str, right.results)).index(str(l[1])) + 1
        if l[0] + 1 in SCORES and r2scr in SCORES:
            res += [[l[1], SCORES[l[0] + 1] + SCORES[r2scr], SCORES[l[0] + 1], SCORES[r2scr], l[0] + 1, r2scr, 0]]

        elif l[0] + 1 in SCORES and r2scr not in SCORES:
            res += [[l[1], SCORES[l[0] + 1], SCORES[l[0] + 1], 0, l[0] + 1, r[0] + 1, 0]]

        elif l[0] + 1 not in SCORES and r2scr in SCORES:
            res += [[l[1], SCORES[r2scr], 0, SCORES[r2scr], l[0] + 1, r[0] + 1, 0]]
        else:
            res += [[l[1], (l[0] + 1 + r[0] + 1) * (-1), 0, 0, l[0] + 1, r[0] + 1], 0]
    # сортировка по второму признаку учитывает собственный вес Спортсмена, при равенстве очков побеждает более легкий
    res=sorted(res, key=lambda a: (-a[1], int(a[0].weight)))
    for checker, i in enumerate(res):
        i[6] = checker + 1

    return res


def save_start(start: dict):
    """сохранение старта в базу"""

    if start_is_end(start):
        no_title = [st for st in start if st not in ("title", "date")]

        for left_hand, right_hand in [(no_title[x], no_title[x + 1]) for x in range(0, len(no_title), 2)]:
            for result in sum_place_of_comp(start[left_hand], start[right_hand]):
                # защита от дубликатов
                filt = AllResults.objects.filter(sportsmen=Armwrestler.objects.get(name=result[0].name),
                                                 competition=AllCompetition.objects.get(title=start['title']))
                if filt:
                    return
                curr_sportsmen = Armwrestler.objects.get(name=result[0].name)
                sp_n_to_save = AllResults(
                    sportsmen=curr_sportsmen,
                    competition=AllCompetition.objects.get(title=start['title']),
                    points=result[1],
                    points_left=result[2],
                    points_right=result[3],
                    left_place=result[4],
                    right_place=result[5],
                    sum_place=result[6],
                    weight_cat=select_category_parcer(curr_sportsmen.weight_category, curr_sportsmen.sex),
                    weight_actual=curr_sportsmen.weight_category
                )

                sp_n_to_save.save()


def competition(request, category):
    # не представленные категории
    # использвуется только если кто то намеренно наберет в адресную строку не юзаную категорию
    if category not in [x[:-1] for x in a]:

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

    # преобразует список объектов по занятым местам в список строк, если сетка завершилась
    result_l = list(map(str, a[category + "l"].results)) if len(a[category + "l"].results) == len(
        a[category + "l"].not_paired_sps) else []
    result_r = list(map(str, a[category + 'r'].results)) if len(a[category + "r"].results) == len(
        a[category + "r"].not_paired_sps) else []
    save_start(a)

    """
    завершение всего старта
    """
    if start_is_end(a):
        cmps = AllCompetition.objects.get(title=a["title"])
        cmps.done = True
        cmps.save()
    return render(request, 'competit.html', {
        "competition_end": start_is_end(a),
        'no_visible': "flex",
        'alert': None,
        "sps_l": a[category + "l"].not_paired_sps,
        "sps_r": a[category + "r"].not_paired_sps,
        "title": a["title"],
        "current_category": CATEGORY_NORMALIZER[category],
        "resa_l": a[category + "l"].return_group_a().split('\n'),  # группа а левая рука в списке
        "resb_l": a[category + "l"].return_group_b().split('\n'),  # группа b левая рука в списке
        "resa_r": a[category + "r"].return_group_a().split('\n'),  # группа а правая рука в списке
        "resb_r": a[category + "r"].return_group_b().split('\n'),  # группа b правая рука в списке
        "resfin_l": a[category + "l"].return_final().split('\n'),  # финальная группа левая рука
        "resfin_r": a[category + "r"].return_final().split('\n'),  # финальная группа правая рука
        "result_l": {i + 1: j for i, j in enumerate(result_l)},  # результаты левая
        "result_r": {i + 1: j for i, j in enumerate(result_r)},  # результаты правая
        "sportsmen1_l": a[category + "l"].sportsmen1,  # текущий спортсмен 1 левой руки
        "sportsmen2_l": a[category + "l"].sportsmen2,  # текущий спортсмен 2 левой руки
        "sportsmen1_r": a[category + "r"].sportsmen1,  # текущий спортсмен 1 правой руки
        "sportsmen2_r": a[category + "r"].sportsmen2,  # текущий спортсмен 2 правой руки
        "is_categories": is_categories,
        'rr': '555',
        'game_over_left': a[category + "l"].game_over * "None",
        'game_over_right': a[category + "r"].game_over * "None",
        # видимость надписи результаты соревнований
        'res_left_vis': (not a[category + "l"].game_over) * "None" or 'block',
        'res_right_vis': (not a[category + "r"].game_over) * "None" or 'block',
    })

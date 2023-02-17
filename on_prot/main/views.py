# from pprint import pprint
from .competition_former import CATEGORY_NORMALIZER
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .competition_former import competition_creating


# Create your views here.

def hello(request):
    return render(request, 'index.html',
                  {
                      "is_categories": is_categories,
                      "title":a["title"]
                  }
                  )


# временно
a = competition_creating("Чемпионат новосибирской области по АРМРЕСТЛИНГУ, ")
print(a)
print("гагарин")
is_categories = sorted(set([x[:-1].replace("+", "plus") for x in a.keys() if x != 'title']))

print(is_categories)


def competition(request, category):
    # не представленные категории

    if category not in [x[:-1] for x in a]:
        print("no_active_" + category)
        return render(request, 'competit.html', {
            'sps_l': "Категория не представлена",
            'no_visible': None,
            'alert': 'block',
            'is_categories': is_categories

        })

    result_l = list(map(str, a[category + "l"].results)) if len(a[category + "l"].results) == len(
        a[category + "l"].not_paired_sps) else []
    result_r = list(map(str, a[category + 'r'].results)) if len(a[category + "r"].results) == len(
        a[category + "r"].not_paired_sps) else []

    if request.method == 'POST':
        # if a[category+'l'].game_over:
        #     print("Игра все!!!!!!!!!!!!!!!!!!!!!!!")
        #     return render(request, 'competit.html', {"result": {i + 1: j for i, j in enumerate(a[category+"l"].results)}})

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

    sp1_l = a[category + "l"].sportsmen1
    sp2_l = a[category + "l"].sportsmen2

    res_gr_a_r = a[category + "r"].return_group_a().split('\n')
    res_gr_b_r = a[category + "r"].return_group_b().split('\n')

    sp1_r = a[category + "r"].sportsmen1
    sp2_r = a[category + "r"].sportsmen2


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
        "result_l": {i + 1: j for i, j in enumerate(result_l)},
        "result_r": {i + 1: j for i, j in enumerate(result_r)},
        "sportsmen1_l": sp1_l,
        "sportsmen2_l": sp2_l,
        "sportsmen1_r": sp1_r,
        "sportsmen2_r": sp2_r,
        "is_categories": is_categories,
        'rr': '555',
        'game_over_left': a[category + "l"].game_over*"None",
        'game_over_right': a[category + "r"].game_over*"None",

    })

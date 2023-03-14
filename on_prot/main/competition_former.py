import datetime

from .comp_n import Sportsmen,Competition
from .models import Armwrestler
#для удобоваримого отображения категорий
CATEGORY_NORMALIZER={
    '50w':"Женщины 50кг",
    '60w':"Женщины 60кг",
    '60m':"Мужчины 60кг",

    '110m':"Мужчины 110кг",
    '+110m':"Мужчины +110кг"

     #доделать!!!
}



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
        return str(mens[-1])
    elif sex == 'w':
        for i in woman:
            if int(category) > 80:
                return "+80"
            if int(category) > i:
                return str(woman[woman.index(i) - 1])
        return str(woman[-1])


def competition_creating(name_of_competition: str,date_of_competition:datetime.datetime,li=Armwrestler.objects.all()):
    """
    создание дикта в котором
    ключ - код турнирной сетки "110lm" например это категория 110, рука левая мужчины
    значение экземаляр соревнования
    """

    def list_of_categories():
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

        #print(f" мужские{m_categories} женские {w_categories}")
        return sorted(m_categories), sorted(w_categories)

    dict_category_sportsmens = {}
    # словарь в котором ключ - категория, а значение список спортсменов

    dict_category_competition = {}

    # словарь в котором ключ - категория, а значение объект соревнования

    def configure_list_of_sportsmen():
        """делает дикт:  категория : список объектов: 'спортсмен данного мероприятия'"""
        # часть формирующая мужскую часть соревнования
        for m_category in list_of_categories()[0]:
            for armwres in Armwrestler.objects.all():
                if select_category_parcer(armwres.weight_category, 'm') == m_category[:-2] and armwres.sex == "m":
                    if m_category not in dict_category_sportsmens:
                        dict_category_sportsmens[m_category] = [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age, armwres.sex, armwres.grade)]
                    else:
                        dict_category_sportsmens[m_category] += [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age, armwres.sex, armwres.grade)]
        # часть формирующая женскую часть соревнования
        for w_category in list_of_categories()[1]:
            for armwres in Armwrestler.objects.all():
                if select_category_parcer(armwres.weight_category, 'w') == w_category[:-2] and armwres.sex == "w":
                    if w_category not in dict_category_sportsmens:
                        dict_category_sportsmens[w_category] = [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age,armwres.team, armwres.sex, armwres.grade)]
                    else:
                        dict_category_sportsmens[w_category] += [
                            Sportsmen(armwres.name, armwres.weight_category, armwres.age,armwres.team, armwres.sex, armwres.grade)]

        #print(dict_category_sportsmens)
        return dict_category_sportsmens

    configure_list_of_sportsmen()
    for cat, sps in dict_category_sportsmens.items():
        dict_category_competition[cat] = Competition(sps, "left", cat, name_of_competition)

    dict_category_competition["title"] = name_of_competition
    dict_category_competition["date"] = date_of_competition

    return dict_category_competition

from pprint import pprint
from random import shuffle

from datetime import datetime


class Sportsmen:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.wins = 0
        self.loses = 0

    def __str__(self):
        return f"{self.name} {self.category}"


class Competition:
    def __init__(self, competitors: list['Sportsmen'] = None, date=datetime.now()):
        if competitors is None:
            competitors = [[]]
        self.current_tour = 1
        self.current_group = 'a'
        self.current_pair = 0
        self.competitors = competitors
        self.date: datetime = date
        self.shuffle_()
        self.group_a: list[list[Sportsmen]] = [list() for x in range(40)]
        self.group_a[0] = competitors
        self.group_b: list[list[Sportsmen]] = [list() for x in range(40)]
        self.results: list['Sportsmen'] = []
        """если количество участников нечетное то последний в списке попадает в следующий тур сразу """
        if not len(competitors) % 2:
            self.group_a[1] += [self.competitors.pop()]

    def __str__(self):
        return ", ".join(str(x) for x in self.competitors)

    """Все таки для защиты от дурака откажусь от редактирования после инициализации"""

    # def __add_sportsmen(self, sportsmen):
    #     self.competitors += sportsmen
    #
    # def __del_sportsmen(self, sportsmen_id):
    #     """Id спортсмена это его номер в списке"""
    #     self.competitors.pop(sportsmen_id)
    def shuffle_(self):
        '''жеребьевка'''
        shuffle(self.competitors)

    def fight(self, winner):

        """текущий боец 1, группы а"""
        current_a_f1 = self.group_a[self.current_tour - 1][self.current_pair]
        """текущий боец 2, группы а"""
        current_a_f2 = self.group_a[self.current_tour - 1][self.current_pair + 1]
        if self.current_group == "a":
            "идем по сетке а"
            if winner == 1:
                self.group_a[self.current_tour] += [current_a_f1]
                self.group_b[self.current_tour] += [current_a_f2]
                current_a_f1.wins += 1
                current_a_f2.loses += 1
            elif winner == 2:
                self.group_a[self.current_tour] += [current_a_f2]
                # print(current_a_f2)
                self.group_b[self.current_tour] += [current_a_f1]
                current_a_f2.wins += 1
                current_a_f1.loses += 1
            self.current_pair += 2

            if self.current_pair > len(self.group_a[self.current_tour-1]):
                self.current_pair = 0
                if self.current_tour != 0:
                    self.current_group = 'b'

        elif self.current_group == 'b':
            "идем по сетке б"
            if winner == 1:
                self.group_b[self.current_tour] += [current_a_f1]
                current_a_f1.wins += 1
                self.results += [current_a_f2]
                self.group_b[self.current_tour].remove(current_a_f2)

            elif winner == 2:
                self.group_b[self.current_tour] += [current_a_f1]
                current_a_f2.wins += 1
                self.results += [current_a_f1]
                self.group_b[self.current_tour].remove(current_a_f2)

            if self.current_pair > len(self.group_a[self.current_tour-1]):
                self.current_pair = 0
                self.current_group = 'a'
                self.current_tour += 1


sp_s = [Sportsmen('витя' + str(i), 50 + i * 5) for i in range(12)]

sorev = Competition(sp_s)


def check():
    print(sorev.current_group + " сетка")
    print(str(sorev.current_tour) + " Тур")
    print(sorev.current_pair)

print(len(sorev.group_a[0]))
sorev.fight(1)
check()
sorev.fight(1)
check()
sorev.fight(1)
check()
sorev.fight(1)
check()
sorev.fight(1)
check()

for i in sorev.group_a:
    for j in i:
        print(str(j), end=", ")
    print()

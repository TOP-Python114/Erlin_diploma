"""
МОдуль движка соревнования, построение сетки по системе после двух поражений
"""

import datetime
from random import randrange,shuffle


class Sportsmen:
    def __init__(self, name: str, weight: float, age: int = 18, team: str = 'Новосибирск', sex='m', grade: str = 'б/р',
                 trainer='самостоятельно'):
        self.name = name
        self.age = age
        self.team = team
        self.weight = weight
        self.sex = sex
        self.grade = grade
        self.trainer = trainer

    def __str__(self):
        return f"{self.name}"


class Competition:
    def __init__(self, sp_s: list, hand: str = 'left', category="65", title='notitle', date_=datetime.datetime.now()):
        self.hand = hand
        self.category = category
        self.begin = False
        #self._date=date_
        self.not_paired_sps = sp_s
        #жеребьевка
        shuffle(sp_s)
        self.sportsmens = self.pairy_list(self.not_paired_sps)
        self.group_a = [list() for _ in range(len(sp_s) + 3)]
        self.group_b = [list() for _ in range(len(sp_s) + 3)]
        self.group = "a"
        self.chitaem = 0
        self.tour = 0
        self.pair = 0
        #результаты
        self.results = []
        #текущий финал
        self.final = []
        # финальная группа, это тоже в общем список списков потому что финалов может быть 2
        self.group_final = []
        self.game_over = False
        self.checker = False
        self.two_losers_in_final = False
        self.did=0

    def print_group_a(self):
        print("Группа А:")
        print("Тур: 0 " + " ".join(a.name for a in self.not_paired_sps))
        for cou, tour in enumerate(self.group_a):
            print(f"Тур: {cou + 1}", end=' ')
            for pairs in range(len(tour)):
                for sportsmen in tour[pairs]:
                    print(sportsmen, end=", ")
            print(" ")
        print(" ")

    def return_group_a(self):
        """ возвращает строкой группу А"""
        res = "Тур: 0 " + " ".join(a.name for a in self.not_paired_sps) + "\n"
        for cou, tour in enumerate(self.group_a):
            if not tour:
                continue
            res += f"Тур: {cou + 1} "
            for pairs in range(len(tour)):
                if isinstance(tour[0], list):
                    for sportsmen in tour[pairs]:
                        res += str(sportsmen) + ", "
                else:
                    res += str(tour[0])
                    try:
                        res += ','
                        res += str(tour[1])
                    except:
                        pass
                    return res
            res += "\n"
        return res

    def return_group_b(self):
        """ возвращает строкой группу Б"""
        # res = "Тур: 0 " + " ".join(a.name for a in self.not_paired_sps) + "\n"
        res = ""
        for cou, tour in enumerate(self.group_b):
            if not tour:
                continue
            res += f"Тур: {cou + 1} "
            for pairs in range(len(tour)):
                if isinstance(tour[0], list):
                    for sportsmen in tour[pairs]:
                        res += str(sportsmen) + ", "
                else:
                    res += str(tour[0])
                    try:
                        res += ', '
                        res += str(tour[1])
                    except:
                        continue
                    return res
            res += "\n"
        return res

    def print_group_b(self):
        print("Группа Б:")
        # print("Тур: 0 " + " ".join(a.name for a in comp.not_paired_sps))
        for cou, tour in enumerate(self.group_b):
            print(f"Тур: {cou + 1}", end=' ')
            for pairs in range(len(tour)):
                for sportsmen in tour[pairs]:
                    print(sportsmen, end=", ")
            print(" ")
        print(" ")

    def print_group_final(self):
        for num, final in enumerate(self.group_final):
            print("финал №" + str(num + 1) + " " + str(final[0][0]), str(final[1][0]))
        print(" ")
    def return_final(self):
        """ возвращает строкой финальную группу"""
        res=""
        for tour,pairs in enumerate(self.group_final):
            res += f'Финал №{tour + 1}: '
            for spm in pairs:
                res+=str(spm[0])
                res+=", "
            res+='\n'
        return res



    def print_results(self):
        for place, sportsmen in enumerate(self.results):
            print(
                f"{place + 1} место: {sportsmen.name}, возраст: {sportsmen.age}, вес: {sportsmen.weight}, тренер: {sportsmen.trainer}")

    @staticmethod
    def is_good(lis):
        """в группе сформированы пары и нет спортсмена в свободном круге"""
        return len(lis[-1]) == 2

    @staticmethod
    def pairy_list(lis):
        """метод разбивающий список на список пар"""
        return [[lis[i], lis[i + 1]] if i + 1 != len(lis) else [lis[i]] for i in range(0, len(lis), 2)]

    @property
    def sportsmen1(self):

        if self.game_over:
            return "Показать результаты"
        """высчитывает имя первого спортсмена"""
        if len(self.not_paired_sps) == 1:
            return self.not_paired_sps[0]

        if len(self.not_paired_sps) == 2 and not self.final:
            return self.not_paired_sps[0]

        if len(self.final) == 2:
            return self.final[0][0]



        # обработка свободного круга

        if self.tour > 0 and len(self.group_a[self.tour - 1][self.pair]) == 1:
            self.fight(1)
            # return self.group_b[self.tour][self.pair][0]

        if self.tour == 0:
            return self.sportsmens[self.pair][0]
        if self.tour > 0:
            if self.group == 'a':
                return self.group_a[self.tour - 1][self.pair][0]

            if self.group == 'b':
                return self.group_b[self.tour - 1][self.pair][0]

    @property
    def sportsmen2(self):
        """высчитывает имя второго спортсмена"""
        if self.game_over:
            return ""
        if len(self.not_paired_sps) == 1:
            return None
        if len(self.not_paired_sps)==2 and not self.final:
            return self.not_paired_sps[1]

        if len(self.final) == 2:
            return self.final[1][0]



        # обработка свободного круга
        # if self.tour > 0 and len(self.group_a[self.tour - 1][self.pair]) == 1:
        #     return self.group_b[self.tour][self.pair][1]

        if self.tour == 0:
            return self.sportsmens[self.pair][1]
        if self.tour > 0:
            if self.group == 'a':
                return self.group_a[self.tour - 1][self.pair][1]

            if self.group == 'b':
                return self.group_b[self.tour - 1][self.pair][1]

    def clear_slots(self):
        """очищает лишние слоты """
        try:
            while self.group_a[-1] == []:
                self.group_a.pop()
            while self.group_b[-1] == []:
                self.group_b.pop()
        except:
            pass

    # КОММЕНТАРИЙ: если код метода разрастается на 200 строк, забитых if-ами, то что-то не так с моделью
    # СДЕЛАТЬ: постройте диаграмму модели и помедитируйте над ней размышляя о том, как бы всё это оптимизировать
    def fight(self, winner):
        """Поединок
            winner== 1- победил спортсмен 1
        """

        if self.game_over:
            return
        # если вего один участник
        if len(self.not_paired_sps) == 1:
            self.results += [self.not_paired_sps[0]]
            self.game_over = True
            return
        #если всего два участника


        if len(self.not_paired_sps) == 2:
            if not self.did:
                if winner == 1:
                    self.final+= [[self.not_paired_sps[0]]]
                    self.final += [[self.not_paired_sps[1]]]
                    self.group_final+=[self.final]
                elif winner == 2:
                    self.final += [[self.not_paired_sps[1]]]
                    self.final += [[self.not_paired_sps[0]]]
                    self.group_final += [self.final]
                self.did=1
                #self.tour+=1
                return

        if len(self.final) == 2:
            self.group_final += [self.final]
            # финал сформирован

            if winner == 1:
                self.results += self.final[1]
                self.results += self.final[0]
                self.game_over = True
                self.results = self.results[::-1]
                self.clear_slots()
                return

            elif winner == 2 and not self.two_losers_in_final:

                self.two_losers_in_final = True

                return

            elif winner == 2:
                self.results += self.final[0]
                self.results += self.final[1]
                self.game_over = True
                self.results = self.results[::-1]
                self.clear_slots()
                return

        """Частный случай первого раунда"""
        #########################################################################################
        # Обработка первого раунда группы А
        #########################################################################################
        if self.tour == 0:
            if not self.is_good(self.sportsmens) and self.checker is False:  # Если есть  в свободном круге
                self.group_a[0] += self.sportsmens[-1]
                self.checker = True
                # Добавляем его в первый раунд группы а

            # для отметки текущих бойцов
            # self.spoprsm1=self.sportsmens[self.pair][0]
            # self.spoprsm2=self.sportsmens[self.pair][1]
            if winner == 1:
                self.group_a[0] += [self.sportsmens[self.pair][0]]
                self.group_b[0] += [self.sportsmens[self.pair][1]]

            elif winner == 2:
                self.group_a[0] += [self.sportsmens[self.pair][1]]
                self.group_b[0] += [self.sportsmens[self.pair][0]]
            # Добавить потом победителя второго
            self.pair += 1
            if self.pair + self.checker >= len(self.sportsmens):
                self.tour += 1
                self.pair = 0
                self.group_a[0] = self.pairy_list(self.group_a[0])
                self.group_b[0] = self.pairy_list(self.group_b[0])
                self.checker = False
        ##########################################################################################
        # </-- конец  #Обработки первого раунда группы А
        ##########################################################################################
        elif self.tour > 0:
            # если это уже второй тур
            if self.group == "a":
                # если мы в группе 'а'
                ####################################################################################
                # ОБРАБОТКА ГРУППЫ А ЕСЛИ ОСТАЛСЯ ОДИН ЧЕЛОВЕК
                ####################################################################################
                if len(self.group_a[self.tour - 1][self.pair]) == 1:
                    # остался один человек в группе а - 'финалист'
                    # if len(self.group_b[self.tour - 1])!=1:
                    self.group_a[self.tour] = self.group_a[self.tour - 1]
                    # переносим его в следующий тур
                    self.pair = 0
                    self.group = 'b'  # переходим в тур б
                    # если в финале никого нет то
                    if not self.final:
                        self.final += self.group_a[self.tour - 1]
                        if len(self.group_b[self.tour - 1][0]) == 1:
                            self.final += self.group_b[self.tour - 1][0]
                    return
                ########################################################################################
                # checker=False #финт со сбободным кругом если checker == True значит мы не смотрим на него в предыдущем туре чтобы формировать пары участников

                ##################################################################################################
                # если в предыдущем туре нечетное количество участников переносим первым участником в следующий тур этого участника
                ##################################################################################################
                if not self.is_good(self.group_a[self.tour - 1]) and not self.checker:
                    # self.group_a[self.tour] += self.group_a[self.tour - 1].pop()
                    self.group_a[self.tour] += self.group_a[self.tour - 1][-1]
                    self.checker = True
                #####################################################################################
                # в зависимости от победителя добавляем победителя в группу а, проигравшего в группу б
                # self.spoprsm1=self.group_a[self.tour - 1][self.pair][0]
                # self.spoprsm2=self.group_a[self.tour - 1][self.pair][0]
                if winner == 1:
                    self.group_a[self.tour] += [self.group_a[self.tour - 1][self.pair][0]]
                    self.group_b[self.tour] += [self.group_a[self.tour - 1][self.pair][1]]
                if winner == 2:
                    self.group_a[self.tour] += [self.group_a[self.tour - 1][self.pair][1]]
                    self.group_b[self.tour] += [self.group_a[self.tour - 1][self.pair][0]]
                self.pair += 1
                # конец добавления в группу а, группу б
                #######################################################################################
                # если количество пар предыдущего тура равно паре текущего тура то:  б обнуляем пару
                if len(self.group_a[self.tour - 1]) <= self.pair + self.checker:
                    self.pair = 0  # обнуляем пару
                    self.group = 'b'  # переходим в группу
                    self.group_a[self.tour] = self.pairy_list(
                        self.group_a[self.tour])  # формируем пары из списка участников
                    self.checker = False  # обнуляем колхоз

            if self.group == "b":
                # если в предыдущем туре нечетное количество участников переносим первым участником в следующий тур этого участника
                ##################################################################################################
                if self.tour > 0:

                    if not self.is_good(self.group_b[self.tour - 1]) and not self.checker:

                        if len(self.group_b[self.tour - 1][self.pair]) == 1 and len(
                                self.group_a[self.tour - 1][self.pair]) != 1:
                            self.group_b[self.tour] += self.group_b[self.tour - 1][self.pair]
                            self.group_b[self.tour] = self.pairy_list(
                                self.group_b[self.tour])  # чет наворотил !!!!!!!!!!!!!!!!!!!!
                            self.group = 'a'
                            self.tour += 1
                            return

                        self.group_b[self.tour] += self.group_b[self.tour - 1][-1]
                        self.checker = True
                #####################################################################################

                if winner == 1:
                    # если побеждает первый, то он добавляется в следующий тур группы Б

                    self.group_b[self.tour] += [self.group_b[self.tour - 1][self.pair][0]]
                    self.results += [self.group_b[self.tour - 1][self.pair][1]]  # проигравший вписывается в протокол

                    # соответсвенно пара предыдущего шага переходит к следующей
                    # self.pair += 1
                if winner == 2:
                    # если побеждает первый, то он добавляется в следующий тур группы Б

                    self.group_b[self.tour] += [self.group_b[self.tour - 1][self.pair][1]]
                    self.results += [self.group_b[self.tour - 1][self.pair][0]]  # проигравший вписывается в протокол
                    # соответсвенно пара предыдущего шага переходит к следующей
                self.pair += 1
                # если пара превышает длину предыдущего тура то проверить
                if self.pair + self.checker == len(self.group_b[self.tour - 1]):
                    if len(self.group_b[self.tour]) == 1:
                        # print("Ща добавим в финал")
                        self.group_b[self.tour] = self.pairy_list(self.group_b[self.tour])

                        self.final += self.group_b[self.tour]

                        return
                    self.checker = False
                    self.group_b[self.tour] = self.pairy_list(self.group_b[self.tour])
                    self.pair = 0
                    self.tour += 1
                    self.group = 'a'



if __name__ == "__main__":
    a = [Sportsmen("sportsmen" + str(i), weight=randrange(120, 150), age=randrange(16, 58), ) for i in range(3)]

    comp = Competition(a)

    print("Тур: 0 " + " ".join(a.name for a in comp.not_paired_sps))
    while not comp.game_over:

        print(" ")

        if len(comp.final) < 2:
            print(f"в группе {comp.group}, в туре №{comp.tour} борятся {comp.sportsmen1} и {comp.sportsmen2}")
        else:
            print(f"Финал {comp.sportsmen1} и {comp.sportsmen2}")

        result = int(input("1 или 2: "))
        if result not in (1, 2):
            print('Ошибка введите 1 если победил первый спортсмен или 2 если второй')
            continue

        comp.fight(result)
        # print(f"победитель {[fighters[result-1]]}")

    # for i in range(360):
    #     comp.fight(1)
    # print("---------------------------------------------")

    print("")
    print("Начало соревн5ований:")
    print("Количество участников: " + str(len(comp.not_paired_sps)))

    print(comp.return_group_a())
    print(comp.return_group_b())
    comp.print_group_final()
    print("Внизу")
    print(comp.return_final())
    print("Результаты соревнований: ")
    comp.print_results()

    # print("раунд №0", end=" ")
    # print(comp.sportsmens)
    # for coui, i in enumerate(comp.group_a):
    #     print("раунд №" + str(coui + 1) + " ", end="")
    #     print(i)
    # print("")
    # print("Группа Б:")
    # for coui, i in enumerate(comp.group_b):
    #     print("раунд №" + str(coui + 1) + " ", end="")
    #     print(i)
    # print("")
    #
    # for place, i in enumerate(comp.results):
    #     print(f" {place + 1} место: {i}")
    #
    #

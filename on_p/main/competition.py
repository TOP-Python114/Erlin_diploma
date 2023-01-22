a = [f'sportsmen{i}' for i in range(35)]
print(a)


class Competition:
    def __init__(self, sp_s: list):
        self.sportsmens = self.pairy_list(sp_s)
        self.group_a = [list() for _ in range(len(self.sportsmens) + 2)]
        self.group_b = [list() for _ in range(len(self.sportsmens) + 2)]
        # self.state=["a",0,0]   #группа, тур, пара
        self.group = "a"
        self.tour = 0
        self.pair = 0
        self.results = []
        self.final = []
        self.game_over = False

    @staticmethod
    def is_good(lis):
        """говорящий что в группе сформированы пары и нет сп-на в свободном круге"""
        return len(lis[-1]) == 2

    @staticmethod
    def pairy_list(lis):
        """разбивающий список на список пар"""
        return [[lis[i], lis[i + 1]] if i + 1 != len(lis) else [lis[i]] for i in range(0, len(lis), 2)]

    def fight(self, winner):
        if self.game_over:
            return
        print(self.final)
        print("сверху финал")
        if len(self.final) == 2:
            if winner == 1:
                print(f"Победитель {self.final[0][0]}")
                self.game_over = True
                return
        "Частный случай первого раунда"
        #########################################################################################

        if self.tour == 0:
            if not self.is_good(self.sportsmens):  # Если есть  в свободном круге
                self.group_a[0] += self.sportsmens.pop()  # Добавляем его в первый раунд группы а
            if winner == 1:
                self.group_a[0] += [self.sportsmens[self.pair][0]]
                self.group_b[0] += [self.sportsmens[self.pair][1]]
            # Добавить потом победителя второго
            self.pair += 1
            if self.pair >= len(self.sportsmens):
                self.tour += 1
                self.pair = 0
                self.group_a[0] = self.pairy_list(self.group_a[0])
                self.group_b[0] = self.pairy_list(self.group_b[0])

        ##########################################################################################
        elif self.tour > 0:
            if self.group == "a":
                if len(self.group_a[self.tour - 1][self.pair]) == 1:
                    self.group_a[self.tour] += self.group_a[self.tour - 1]
                    self.pair = 0
                    self.group = 'b'
                    # self.tour+=1
                    if not self.final:
                        self.final += self.group_a[self.tour - 1]
                    return
                if not self.is_good(self.group_a[self.tour - 1]):
                    self.group_a[self.tour] += self.group_a[self.tour - 1].pop()
                if winner == 1:
                    self.group_a[self.tour] += [self.group_a[self.tour - 1][self.pair][0]]
                    self.group_b[self.tour] += [self.group_a[self.tour - 1][self.pair][1]]
                self.pair += 1
                if len(self.group_a[self.tour - 1]) <= self.pair:
                    self.pair = 0
                    self.group = 'b'
                    self.group_a[self.tour] = self.pairy_list(self.group_a[self.tour])

            if self.group == "b":

                if winner == 1:
                    # если побеждает первый, то он добавляется в следующий тур группы Б
                    self.group_b[self.tour] += [self.group_b[self.tour - 1][self.pair][0]]
                    # соответсвенно пара предыдущего шага переходит к следующей
                    self.pair += 1
                # если пара превышает длину предыдущего тура то
                if self.pair == len(self.group_b[self.tour - 1]):
                    if len(self.group_b[self.tour]) == 1:
                        self.final += [self.group_b[self.tour]]
                        print("Гаме овер")
                        return

                    self.group_b[self.tour] = self.pairy_list(self.group_b[self.tour])
                    self.pair = 0
                    self.tour += 1
                    self.group = 'a'


comp = Competition(a)
comp2 = Competition(a)
print(comp.sportsmens)
for i in range(360):
    comp.fight(1)
print("---------------------------------------------")

print("")
print("Начало соревн5ований:")
print("Группа А")
for coui, i in enumerate(comp.group_a):
    print("раунд №" + str(coui + 1) + " ", end="")
    print(i)
print("")
print("Группа Б:")
for coui, i in enumerate(comp.group_b):
    print("раунд №" + str(coui + 1) + " ", end="")
    print(i)

print(comp.final)  #
# print("____________")
# print("Начало соревн5ований:")
# print("Группа А")
# for coui, i in enumerate(comp2.group_a):
#     print("раунд №" + str(coui + 1) + " ", end="")
#     print(i)
# print("")
# print("Группа Б:")
# for coui, i in enumerate(comp2.group_b):
#     print("раунд №" + str(coui + 1) + " ", end="")
#     print(i)

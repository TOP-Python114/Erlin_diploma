from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Armwrestler(models.Model):
    """
    модель спортсмена рукоборца
    """
    name = models.CharField(max_length=100)
    # ИСПРАВИТЬ здесь и далее: для моделей, которые получают данные только из пользовательского ввода валидация производится в формах
    age = models.PositiveIntegerField()
    weight_category = models.CharField(max_length=4)
    team = models.CharField(max_length=54)
    sex = models.CharField(max_length=2)
    grade = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.name} {self.weight_category} {self.sex} {self.grade}"




class AllCompetition(models.Model):
    """
    модель соревнования
    """
    title = models.CharField(max_length=100)
    date = models.DateField()
    done = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} {self.date} соревнования {not self.done and 'не' or ' '}прошли"




class SportsmenRegistration(models.Model):
    competition=models.ForeignKey(AllCompetition,on_delete=models.CASCADE)
    sportsmen=models.ForeignKey(Armwrestler,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.competition} ---- {self.sportsmen}"

class AllResults(models.Model):
    """
    модель результатов соревнований
    """
    sportsmen = models.ForeignKey(Armwrestler, on_delete=models.CASCADE)
    competition = models.ForeignKey(AllCompetition, on_delete=models.CASCADE)
    points=models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(50)],default=0)
    points_left=models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(25)],default=0)
    points_right = models.IntegerField(validators=[MinValueValidator(-100), MaxValueValidator(25)], default=0)
    left_place = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=100)
    right_place = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=100)
    sum_place= models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)],default=100)
    weight_cat=models.CharField(max_length=4, default="60")
    weight_actual=models.CharField(max_length=4, default="60")

    def __str__(self):
        return f' Сооревнование: {self.competition.title} Спортсмен: {self.sportsmen}, Левая "{self.left_place} ' \
               f'место" правая "{self.right_place}место"- по сумме:{self.sum_place} ' \
               f' очки с:{self.points} л:{self.points_left} п: {self.points_right}'

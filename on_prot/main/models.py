from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Armwrestler(models.Model):
    """
    модель спортсмена рукоборца
    """
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(67)])
    weight_category = models.CharField(max_length=4, default='60')
    team = models.CharField(max_length=54, default='Новосибирск')
    sex = models.CharField(max_length=2, default='m')
    grade = models.CharField(max_length=4, default='б/р')

    def __str__(self):
        return f"{self.name} {self.weight_category} {self.sex} {self.grade}"






class Competition(models.Model):
    """
    надо убрать
    """
    HANDS = [("left", "сетка по левым рукам"), ("r", "сетка по правым рукам")]
    SEX = [('men', "среди мужчин"), ('women', "среди женщин")]
    CATEGORIES = [('50', '50'),
                  ('55', '55'),
                  ('60', '60'),
                  ('65', '65'),
                  ('70', '70'),
                  ('75', '75'),
                  ('80', '80'),
                  ('85', '85'),
                  ('90', '90'),
                  ('100', '100'),
                  ('110', '110'),
                  ('+110', '+110'),
                  ('+80', '+80')]

    sex = models.CharField(max_length=5, choices=SEX, default='men')
    category = models.CharField(max_length=5, choices=CATEGORIES, default="50")
    hand = models.CharField(max_length=5, choices=HANDS, default='left')
    title = models.CharField(max_length=100)
    sportsmens = models.ManyToManyField(Armwrestler)



class AllCompetition(models.Model):
    """
    модель соревнования
    """
    title = models.CharField(max_length=100)
    date = models.DateField()
    def __str__(self):
        return f"{self.title} {self.date}"

class SportsmenRegistration(models.Model):
    competition=models.ForeignKey(AllCompetition,on_delete=models.CASCADE)
    sportsmen=models.ForeignKey(Armwrestler,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.competition} ---- {self.sportsmen}"

class AllResults(models.Model):
    """
    модель результатов соревнований
    """
    title_competition = models.CharField(max_length=100)
    date = models.DateField()
    sportsmen = models.CharField(max_length=100)
    sex=models.CharField(max_length=4,default='m')
    category = models.CharField(max_length=4)
    hand = models.CharField(max_length=5)
    place = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    def __str__(self):
        return f'{self.date} {self.title_competition} рука: "{self.hand}" {self.place}место- {self.sportsmen}'

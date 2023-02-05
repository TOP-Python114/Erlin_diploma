from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Armwrestler(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(67)])
    weight_category = models.CharField(max_length=4, default='60')

    def __str__(self):
        return f"{self.name} {self.weight_category}"


class Competition(models.Model):
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
    title = models.CharField(max_length=100)
    date = models.DateField()
    content = models.ForeignKey(Competition,on_delete=models.CASCADE)

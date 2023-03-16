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




class AllCompetition(models.Model):
    """
    модель соревнования
    """
    title = models.CharField(max_length=100)
    date = models.DateField()
    done = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.title} {self.date} соревнования {not self.done and 'не' or ''}прошли"




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
    hand = models.CharField(max_length=5)
    place = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])



    def __str__(self):
        return f' {self.competition} рука: "{self.hand}" {self.place}место- {self.sportsmen}'

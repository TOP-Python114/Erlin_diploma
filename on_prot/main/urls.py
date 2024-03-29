from django.contrib import admin
from django.urls import path
from .views import hello, competition, reg_competition, reg_sportsmen, competition_constructor, protocols, new_sportsmen

# from .models import Competition

urlpatterns = [
        path('', hello, name="hello"),


]
def update_patterns(urlpatterns=urlpatterns):
    urlpatterns2=[
        path('reg_comp/',reg_competition,name='rc'),
        path('protocol/', protocols, name='pc'),
        path('sp_n_comp/',reg_sportsmen,name='rs'),
        path('crt', competition_constructor,name='cs'),
        path('new_sportsmen_registration', new_sportsmen, name='ns'),
        path('<category>', competition),
        path('65m',competition,name='tempcpt')
        ]
    urlpatterns+=urlpatterns2


update_patterns()

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

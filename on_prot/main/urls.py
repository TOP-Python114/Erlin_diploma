from django.contrib import admin
from django.urls import path
from .views import hello, competition, reg_competition, reg_sportsmen, competition_constructor

# from .models import Competition

urlpatterns = [
        path('', hello, name="hello"),


]
def update_patterns(urlpatterns=urlpatterns):
    urlpatterns2=[
        path('reg_comp/',reg_competition,name='rc'),
        path('sp_n_comp/',reg_sportsmen,name='rs'),
        path('crt', competition_constructor,name='cs'),

        # path('50w/', competition, name="50w", kwargs={'category': '50w'}),
        # path('55w/', competition, name="55w", kwargs={'category': '55w'}),
        # path('60w/', competition, name="60w", kwargs={'category': '60w'}),
        # path('65w/', competition, name="65w", kwargs={'category': '65w'}),
        # path('70w/', competition, name="70w", kwargs={'category': '70w'}),
        # path('75w/', competition, name="75w", kwargs={'category': '75w'}),
        # path('80w/', competition, name="80w", kwargs={'category': '80w'}),
        # path('plus80w/', competition, name="plus80w", kwargs={'category': '+80w'}),
        # path('55m/', competition, name="55m", kwargs={'category': '55m'}),
        # path('60m/', competition, name="60m", kwargs={'category': '60m'}),
        # path('65m/', competition, name="65m", kwargs={'category': '65m'}),
        # path('70m/', competition, name="70m", kwargs={'category': '70m'}),
        # path('75m/', competition, name="75m", kwargs={'category': '75m'}),
        # path('80m/', competition, name="80m", kwargs={'category': '80m'}),
        # path('85m/', competition, name="85m", kwargs={'category': '85m'}),
        # path('90m/', competition, name="90m", kwargs={'category': '90m'}),
        # path('100m/', competition, name="100m", kwargs={'category': '100m'}),
        # path('110m/', competition, name="110m", kwargs={'category': '110m'}),
        # path('+110m/', competition, name="plus110m", kwargs={'category': '+110m'}),]
        ]
    urlpatterns+=urlpatterns2


  #  path('110m/', competition_r, name="110m", kwargs={'category_r': '110rm'}),

    # path('', admin.site.urls),

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

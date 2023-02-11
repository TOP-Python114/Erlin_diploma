from django.contrib import admin
from django.urls import path
from .views import hello, competition
#from .models import Competition.C
urlpatterns = [
    path('',hello, name="hello"),
    path('competition',competition, name="comp"),
    #path('', admin.site.urls),
]

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






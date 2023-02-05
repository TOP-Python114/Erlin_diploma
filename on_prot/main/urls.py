from django.contrib import admin
from django.urls import path
from .views import hello, competition

urlpatterns = [
    path('',hello, name="hello"),
    path('competition',competition, name="comp"),
    #path('', admin.site.urls),
]

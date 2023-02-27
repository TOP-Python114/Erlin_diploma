from django.contrib import admin
from .models import Armwrestler,Competition,AllResults,AllCompetition,SportsmenRegistration
# Register your models here.
admin.site.register(Armwrestler)
admin.site.register(Competition)
admin.site.register(AllResults)
admin.site.register(AllCompetition)
admin.site.register(SportsmenRegistration)
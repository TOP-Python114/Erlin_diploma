from django.contrib import admin


from .models import Armwrestler, AllCompetition, SportsmenRegistration, AllResults

# Register your models here.
admin.site.register(Armwrestler)
admin.site.register(AllResults)
admin.site.register(AllCompetition)
admin.site.register(SportsmenRegistration)

from django.urls import path
from .views import tr_register, trainers, list_of_trainers, index, tournament
from .models import Armwrestler, Trainer

urlpatterns = [
    path('', index, name='main'),
    path('tr_register', tr_register, name='tr_reg'),
    path('trainers', list_of_trainers, name='sps'),
    path('tournament', tournament, name='trmt'),
]

for trainer in Trainer.objects.all():
    urlpatterns += [
        path(trainer.en_view,
             trainers,
             kwargs={'pk': trainer.id})
    ]



from django.urls import path

from brodyapp.views import hiyo_world

app_name = 'brodyapp'

urlpatterns =[
    path('hiyo_world/', hiyo_world, name = 'hiyo_world')
]
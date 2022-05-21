from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('',views.player,name="player"),
    path('snake/',views.snake,name="snake"),
    path('ttt/',views.ttt,name="ttt"),
    path('flyingb/',views.flyingb,name="flyingb"),
    path('handc/',views.handc,name="handc"),
    path('car/',views.car,name="car"),
]

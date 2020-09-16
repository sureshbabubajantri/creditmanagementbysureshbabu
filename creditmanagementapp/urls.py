from django.urls import path
from . import views

from .views import *
urlpatterns = [
    path('',views.home,name="index"),
    path('home',views.home,name="home"),
    path('viewuser',views.viewuser,name="viewuser"),
    path('transfer/<str:name>',views.transfer,name="transfer"),
    path('transfer',views.transfer,name="transfer"),
    path('transfer/<str:name>/confirmation',views.confirmation,name="confirmation"),
    path('transfertable',views.transfertable,name="transfertable")
    ]
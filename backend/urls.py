from django.urls import include, path
from rest_framework import routers
from . import views #views.py import
#itemviewset 과 item이라는 router 등록

urlpatterns = [
    path('qr/', views.qr, name="qr"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('Store/', views.Store, name="Store"),
    path('point/', views.point, name="point"),
    path('inquiry/', views.inquiry, name="inquiry"),
    path('map/', views.map, name="map"),
    path('addr/', views.addr, name="addr"),
]
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.IndexPage,name="indexpage"),
    path('getcard/',views.GetCardId,name="getcard"),
]
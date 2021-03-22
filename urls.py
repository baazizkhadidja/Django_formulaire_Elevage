from django.urls import re_path
from . import views

urlpatterns = [
    re_path('hello/', views.hello, name = "hello"),
    re_path('', views.home, name = "home"),
]



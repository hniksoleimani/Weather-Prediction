from django.urls import path
from . import views
urlpatterns = [
    path('base', views.base, name="base"),
    path('about', views.about, name="about"),
    path('', views.home, name="home"),

]

from django.urls import path
from . import views
# from pass_website.user_data import views as us_views

urlpatterns = [
    path('', views.home, name="home"),

]

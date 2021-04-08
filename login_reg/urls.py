from django.urls import path
from . import views
# from pass_website.user_data import views as us_views

urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.reg, name="reg"),
    path('logout', views.logout, name="rlogout"),

]

from django.urls import path
from . import views




urlpatterns = [
    path('', views.home,name="home"),
    path('signup/', views.products,name="signup"),
    path('login/', views.customer, name="login"),
    path('register/', views.register, name="register"),
    path('registerInfo/', views.registerInfo, name="registerInfo"),
    path('underweight/', views.underweight, name="underweight"),
    path('overweight/', views.overweight, name="overweight"),
]
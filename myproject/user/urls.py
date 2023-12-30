from django.urls import path
from . import views

urlpatterns = [
    #1'0
    path('', views.home),
    path('home/', views.home),
    path('about/', views.about),
    path('services/', views.services),
    path('SignUp', views.SignUp),
    path('Login', views.Login),
    path('Contact', views.Contact),
    path('video/', views.videogallery),
    path('viewsnews/', views.newsd),
    path('viewmore/', views.viewmore),
    path('Attacks/', views.Attacks),
    path('Devices/', views.Devices),
    path('Country/', views.Country),
    path('IT News/', views.IT_News),
]


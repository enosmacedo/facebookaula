from django.urls import path, include
from . import views


urlpatterns = [

    path('jessica/', views.teste),
    path('jessica2/', views.teste2)

]

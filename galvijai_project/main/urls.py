from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:pk>/', views.animal_detail, name='animal_detail'),
]
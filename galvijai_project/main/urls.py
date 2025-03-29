from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/<int:pk>/', views.animal_detail, name='animal_detail'),
    path('new_animal/', views.new_animal, name='new_animal'),
    path('animals/<int:animal_id>/add_event/', views.add_event, name='add_event'),
    path('passport/', views.passport, name='passport'),
    path('order_passport/<int:animal_id>/', views.order_passport, name='order_passport'),
    path('ordered_passports/', views.ordered_passports, name='ordered_passports'),
    path('isagai/', views.isagai, name='isagai'),
    path('ataskaitos/', views.ataskaitos, name='ataskaitos'),
]
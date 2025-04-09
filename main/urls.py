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
    path('isagai/', views.isagai, name='isagai'),
    path('order_isagai/<int:animal_id>/', views.order_isagai, name='order_isagai'),
    path('ordered_isagai/', views.ordered_isagai, name='ordered_isagai'),
    path('ataskaitos/', views.ataskaitos, name='ataskaitos'),
    path('animal_search/', views.animal_search, name='animal_search'),
    path('export/pdf/gender/', views.export_by_gender_pdf, name='export_by_gender_pdf'),
    path('export/pdf/color/', views.export_by_color_pdf, name='export_by_color_pdf'),
    path('export/pdf/birth/', views.export_birth_count_pdf, name='export_birth_count_pdf'),
]
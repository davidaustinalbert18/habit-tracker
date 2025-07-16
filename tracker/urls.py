# tracker/urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='tracker/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('create/', views.create_habit, name='create_habit'),
    path('complete/<int:habit_id>/', views.mark_completed, name='mark_completed'),
    path('uncomplete/<int:habit_id>/', views.unmark_completed, name='unmark_completed'),
    path('edit/<int:habit_id>/', views.edit_habit, name='edit_habit'),
    path('delete/<int:habit_id>/', views.delete_habit, name='delete_habit'),
    path('stats/', views.stats, name='stats'),

]

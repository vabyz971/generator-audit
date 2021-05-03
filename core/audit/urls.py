from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *





app_name='audit'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sign-up/', RegisterUserView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='audit/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add-audit/', AddAuditView.as_view(), name="add_audit"),
    path('audit/<pk>/', DetailView.as_view(), name="audit"),
    path('delete-audit/<pk>/', DeteleAuditView.as_view(), name="delete_audit")
]
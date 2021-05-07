from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *





app_name='audit'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sign-up/', RegisterUserView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='audit/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('audit/', AuditListView.as_view(), name="list-audit"),
    path('add-audit/', AddAuditView.as_view(), name="add-audit"),
    path('audit-detail/<int:pk>/', AuditDetailView.as_view(), name="detail-audit"),
]
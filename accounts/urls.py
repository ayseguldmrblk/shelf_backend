import accounts.views
from .views import *
from django.urls import path, include, re_path

urlpatterns = [
    path('users/', accounts.views.CustomUserListView.as_view(), name="users"),
    path('reports/', accounts.views.ReportsView.as_view(), name="reports"),
    path('register/', accounts.views.Register.as_view(), name="register"),
    #path('login/', accounts.views.Login.as_view(), name="login"),
    path('users/<int:pk>/', accounts.views.CustomUserDetailView.as_view(), name="user-detail")
]

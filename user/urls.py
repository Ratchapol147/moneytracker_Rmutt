from user import views
from django.urls import path

urlpatterns = [
    path('login',views.login),
    path('register',views.register),
    path('logout',views.logout),
]
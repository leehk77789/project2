from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path("users/signup/", views.signup, name='signup'),
    path("users/signin/", views.login, name='signin'),
    path("users/logout/", views.logout, name='logout'),
    path("", views.index, name='index'),
    path("users/main/", views.main, name='main'),
]

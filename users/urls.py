from django.urls import path, include
from users import views

app_name = 'users'

urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("signin/", views.login, name='signin'),
    path("index/", views.index, name='index'),
    path("main/", views.main, name='main')
]

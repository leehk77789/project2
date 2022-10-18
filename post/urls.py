from django.urls import path, include
from post import views

app_name = 'post'

urlpatterns = [
    path("upload/", views.upload, name='upload'),
]

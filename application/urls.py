from django.urls import path

from . import views

app_name = "application"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:myid>/", views.view, name="detail"),
]

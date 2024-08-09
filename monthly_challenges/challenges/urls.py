from django.urls import path
from . import views

# It's important to add int:month path first
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]

from django.urls import path
from .views import student, model_student,profile


urlpatterns = [
    path("student/", model_student, name="student"),
    path("", student, name="home"),
    path("profile/", profile, name="profile")
]
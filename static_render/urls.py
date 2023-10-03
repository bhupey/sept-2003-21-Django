from django.urls import path
from .views import static_home,index


urlpatterns=[
    path('index/', index),
    path("",static_home),
]
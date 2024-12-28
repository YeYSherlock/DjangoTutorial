from django.urls import path

from . import views

# url conf
urlpatterns = [
    path("january", views.index), 
]


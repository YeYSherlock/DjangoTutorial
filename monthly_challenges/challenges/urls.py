from django.urls import path

from . import views

# url conf, pattern matching
urlpatterns = [

    # 1 is still a string, so have to be first
    # name is the path's name, to avoid keep using the same name. 
    path("<int:month>", views.monthly_challenges_by_int),
    path("<str:month>", views.monthly_challenges_by_string, name="monthly-challenges")
]


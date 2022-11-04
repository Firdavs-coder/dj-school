from django.urls import path
from school_app.views import *

urlpatterns = [
    path("", home_page, name="home"),
    path("classes/", classes, name="classes"),
    path("teachers/", teachers, name="teachers"),
    path("schedule/", schedule, name="schedule"),
    path("contact/", contact, name="contact"),
]

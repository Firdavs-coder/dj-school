from django.shortcuts import render
from school_app.models import *
# Create your views here.


def home_page(request):
    return render(request, "index.html", {})


def classes(request):
    classes = Classes.objects.all()
    context = {"classes": classes}
    return render(request, "classes.html", context)


def teachers(request):
    return render(request, "teachers.html", {})


def schedule(request):
    return render(request, "schedule.html", {})


def contact(request):
    return render(request, "contacts.html", {})

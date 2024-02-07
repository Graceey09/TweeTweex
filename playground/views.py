from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def welcome(request):
    return HttpResponse("welcome to django")


def hello_world(request, name):
    return render(request, template_name='hello.html', context={"name": name})


def number(request, number):
    return render(request, template_name='number.html', context={"number": number})

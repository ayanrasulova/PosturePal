from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, 'posturepal/index.html')

def live_checker(request):
    return render(request, 'posturepal/live_checker.html')

def about_us(request):
    return render(request, 'posturepal/about_us.html')

def resources(request):
    return render(request, 'posturepal/resources.html')
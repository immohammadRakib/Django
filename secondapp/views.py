from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def courses(request):
    return HttpResponse('There is all courses')

def feedback(request):
    return HttpResponse('This is feedback page')
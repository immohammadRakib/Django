from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def contract(request):
    return HttpResponse("""
                        <h2>This is my contract page</h2>
                        <a href='/fristapp/about/'>About</a>
                        """)

def about (reqest):
    return HttpResponse("""
                        <h2>This is my about page</h2>
                        <a href='/fristapp/contract/'>Courses</a>
                        """)
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def courses(request):
    return HttpResponse("""
                        <h2>There is all courses</h2>
                        <a href='/secondapp/feedback/'>Feedback</a>
                        """)

def feedback(request):
    return HttpResponse("""
                        <h2>This is feedback page</h2>
                        <a href='/secondapp/courses/'>Courses</a>
                        """)
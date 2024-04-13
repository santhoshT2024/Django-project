from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def homepage(request):         # Don't set just "a1.html"
    return render(request, "signup.html")
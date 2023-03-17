from django.shortcuts import render, HttpResponse,redirect
from app1.models import Login
# Create your views here.
from .form import Login_page

def home(request):
    if request.method == 'POST':


        return render(request, "home.html", {"form" : Login_page()})
    elif request.method == 'GET':
        return render(request, "home.html")
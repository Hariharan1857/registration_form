from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import  CreateUserForm
# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def register(request):
    form = CreateUserForm()


    return render(request,"register.html",{'form':form})
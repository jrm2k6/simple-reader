from django.shortcuts import render, get_object_or_404
from simplereader_client.forms import ReaderUserCreationForm
from simplereader_client.models import ReaderUser
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm


def home(request):
    text = "Hello, world. You're at the poll index."
    return render(request, 'home.html', {'text': text})


def auth(request):
    return render(request, 'authentication.html', {'form': ReaderUserCreationForm()})


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            new_user = authenticate(email=request.POST['username'], password=request.POST['password'])
            login(request, new_user)
            return HttpResponseRedirect("/")
        else:
            form = AuthenticationForm()
    else:
        form = AuthenticationForm()
    return render(request, 'authentication.html', {'form': ReaderUserCreationForm(), 'signinForm': form})
    

def signup(request):
    if request.method == 'POST':
        form = ReaderUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(email=request.POST['email'], password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect("/")
    return render(request, 'authentication.html', {'form': ReaderUserCreationForm(), 'signinForm': AuthenticationForm()})


def signout(request):
    logout(request)
    return HttpResponseRedirect('/signin/')


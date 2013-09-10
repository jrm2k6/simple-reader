from django.shortcuts import render, get_object_or_404
from simplereader_client.admin import ReaderUserCreationForm
from simplereader_client.models import ReaderUser


def home(request):
    text = "Hello, world. You're at the poll index."
    return render(request, 'home.html', {'text': text})

def auth(request):
    return render(request, 'authentication_bis.html', {'form': ReaderUserCreationForm()})

def signup(request):
    if request.method == 'POST':
        form = ReaderUserCreationForm(request.POST)
        if form.is_valid():
            print form.cleaned_data
            new_user = form.save()
    return render(request, 'authentication_bis.html', {'form': ReaderUserCreationForm()})

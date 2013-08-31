from django.shortcuts import render, get_object_or_404

def home(request):
    text = "Hello, world. You're at the poll index."
    return render(request, 'home.html', {'text': text})

def auth(request):
    return render(request, 'authentication.html')
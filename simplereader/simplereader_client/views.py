from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def home(request):
    text = "Hello, world. You're at the poll index."
    return render(request, 'home.html', {'text':text})
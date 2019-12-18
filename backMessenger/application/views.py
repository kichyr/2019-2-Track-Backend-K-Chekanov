from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import os
from .settings import BASE_DIR

@login_required
def home(request):
    with open(os.path.join(BASE_DIR, 'static', 'index.html')) as file:
        return HttpResponse(file.read())
def login(request):
    return render(request, "login.html", {}, status=200)
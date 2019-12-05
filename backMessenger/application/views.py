from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, "index.html", {}, status=200)

def login(request):
    return render(request, "login.html", {}, status=200)
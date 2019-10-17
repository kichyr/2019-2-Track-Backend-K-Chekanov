from django.shortcuts import render
from django import JsonResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def chat_detail(request, pk):

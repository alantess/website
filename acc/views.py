from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'acc/dashboard.html')


def main(request):
    return render(request, 'acc/welcome.html')

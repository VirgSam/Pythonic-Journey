from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    """
    homepage of our website
    """
    return HttpResponse('Hello World')

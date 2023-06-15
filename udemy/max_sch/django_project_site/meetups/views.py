from django.shortcuts import render


# Create your views here.

def index(request):
    """
    homepage of our website
    """
    return render(request, 'meetups/index.html') # return index.html

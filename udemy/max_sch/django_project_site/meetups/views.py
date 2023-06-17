from django.shortcuts import render


# Create your views here.

def index(request):
    """
    homepage of our website
    """
    meetups = [
        {'title':'A First meetup'},
        {'title':'A Second meetup'},
    ]
    return render(request, 'meetups/index.html',{
        'meetups': meetups,
        'show_meetups': False,
    }) # return index.html

from django.shortcuts import render
from .models import Meetup


# Create your views here.

def index(request):
    """
    homepage of our website
    """
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html',{
        'meetups': meetups,
        
    }) # return index.html

def meetup_detail(request, meetup_slug):
    """
    Meetup details
    """
    selected_meetups = {
            'title':'A First Meetup',            
            'description':'This is the first meetup',            
        }
    
    return render(request,'meetups/meetup-items.html',{
        'title':selected_meetups['title'],
        'description':selected_meetups['description'],
    })
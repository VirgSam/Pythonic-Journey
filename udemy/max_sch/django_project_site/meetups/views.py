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
    try:
        selected_meetups = Meetup.objects.get(slug=meetup_slug)
        return render(request,'meetups/meetup-items.html',{
        'meetup_found':True,
        'meetup':selected_meetups
    })
    except Exception as exc:
        return render(request,'meetups/meetup-items.html',{
        'meetup_found':False,
        'description':selected_meetups.description,
    })

    
    


    
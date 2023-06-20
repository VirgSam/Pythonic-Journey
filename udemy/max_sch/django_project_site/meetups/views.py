from django.shortcuts import render


# Create your views here.

def index(request):
    """
    homepage of our website
    """
    meetups = [
        {'title':'A First meetup', 'Location':'New York','slug':'a-first-meetup'},
        {'title':'A Second meetup', 'Location':'Berlin','slug':'a-second-meetup'},
        
    ]
    return render(request, 'meetups/index.html',{
        'meetups': meetups,
        'show_meetups': True,
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
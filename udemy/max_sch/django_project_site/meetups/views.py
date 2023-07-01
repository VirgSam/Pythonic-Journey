from django.shortcuts import render
from .models import Meetup
from .forms import RegistrationForm


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
        if request.method == "GET":
            registration_form = RegistrationForm()
            return render(request,'meetups/meetup-items.html',{
            'meetup_found':True,
            'meetup':selected_meetups,
            'form': registration_form,
            })
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                participant=registration_form.save()
                selected_meetups.participants.add(participant)


    except Exception as exc:
        return render(request,'meetups/meetup-items.html',{
        'meetup_found':False,
        'description':selected_meetups.description,
    })

    
    


    
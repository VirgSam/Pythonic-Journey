from django.shortcuts import render, redirect
from .models import Meetup,Participant
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
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email=registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetups.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request,'meetups/meetup-items.html',{
        'meetup_found':True,
        'meetup':selected_meetups,
        'form':registration_form,
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })
        
def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request,'meetups/registration-success.html',{"organiser_email":meetup.organiser_email} )    
    


    
from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), #our_domain_name/meetups
    path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
    path('meetups/<slug:meetup_slug>', views.meetup_detail, name='meetup-detail'),#our_domain_name/meetups/dynamic path segment
     
]
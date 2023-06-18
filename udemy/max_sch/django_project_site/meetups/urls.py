from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index), #our_domain_name/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_detail), #our_domain_name/meetups/dynamic path segment
]
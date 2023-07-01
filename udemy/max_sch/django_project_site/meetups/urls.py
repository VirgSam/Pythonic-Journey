from django.urls import path
from . import views

urlpatterns = [
    path('meetups/', views.index, name='all-meetups'), #our_domain_name/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_detail, name='meetup-detail'),
    path('meetups/confirm_registration', views.confirm_registration, name='confirm-registration'), #our_domain_name/meetups/dynamic path segment
]
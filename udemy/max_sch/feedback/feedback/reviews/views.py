from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewFORM
from django.views import View
#from .models import Review

# Create your views here.
class ReviewView(View):

def review(request):
    """
    Views as functions
    """
    if request.method == "POST":
       form = ReviewFORM(request.POST)
       if form.is_valid():
        #   re_review = Review(user_name=form.cleaned_data['user_name'],
        #                      review=form.cleaned_data['review'],
        #                      ratings=form.cleaned_data['ratings'])
        #  re_review.save() the old way
        form.save() # saving with the modelform utilizing its greater functionality over Review(models.Model)
        return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewFORM()
    return render(request,"reviews/review.html",{"form":form})

def thank_you(request):
    return render(request,"reviews/thank_you.html")
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewFORM

# Create your views here.

def review(request):
    if request.method == "POST":
       form = ReviewFORM(request.POST)
       if form.is_valid():
          print(form.cleaned_data)
          return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewFORM()
    return render(request,"reviews/review.html",{"form":form})

def thank_you(request):
    return render(request,"reviews/thank_you.html")
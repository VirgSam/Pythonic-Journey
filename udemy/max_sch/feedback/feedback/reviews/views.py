from typing import Any
from django.db import models
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ReviewFORM
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView 

# Create your views here.
# Using the class View approach
# class ReviewView(View):
#    """
#    Views as classes to control in detail how your form is rendered
#    """
#    def get(self,request):
#       form = ReviewFORM()
#       return render(request,"reviews/review.html",{"form":form})
   
#    def post(self,request):
#       form = ReviewFORM(request.POST)
#       if form.is_valid():
#          form.save()
#          return HttpResponseRedirect("/thank-you")
#       return render(request,"reviews/review.html",{"form":form})
#
# Using the FormView approach
# class ReviewView(FormView):
#    """
#    How to use the Form View
#    """
#    form_class = ReviewFORM
#    template_name = "reviews/review.html" #{the section makes the get method above redundant}
#    success_url = "/thank-you" #{the section makes the post method above redundant}

#    def form_valid(self, form):#{the section deals with the validation and storing of your data as above}
#        form.save()
#        return super().form_valid(form)

# Using the CreateView 
class ReviewView(CreateView):
   """
   How to use the Create View in comparison to the Form
   """
   model= Review
   form_class = ReviewFORM
   template_name = "reviews/review.html"
   success_url = "/thank-you" #{Create view will automatically validate and save your date, making form_valid redundant}
   

# Using the View function
# def review(request):
#     """
#     Views as functions
#     """
#     if request.method == "POST":
#        form = ReviewFORM(request.POST)
#        if form.is_valid():
#         #   re_review = Review(user_name=form.cleaned_data['user_name'],
#         #                      review=form.cleaned_data['review'],
#         #                      ratings=form.cleaned_data['ratings'])
#         #  re_review.save() the old way
#         form.save() # saving with the modelform utilizing its greater functionality over Review(models.Model)
#         return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewFORM()
#     return render(request,"reviews/review.html",{"form":form})

# Using the View class
# class ThankYouView(View):
#    """
#    Thank you View in class representation
#    """
#    def get(self, request):
#       return render(request,"reviews/thank_you.html")

# Using the TemplateView
class ThankYouView(TemplateView):
   template_name = "reviews/thank_you.html"

   def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         context["message"] = "A message was input into the context dictionary"
         return context

# using the Template view as a list capture mechanism
# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#          context = super().get_context_data(**kwargs)
#          reviews = Review.objects.get(**kwargs)
#          context["reviews"]= reviews
#          return context

# using the List view as a list capture mechanism
class ReviewListView(ListView):
    """
    Simpler approach than above
    """
    template_name = "reviews/review_list.html"
    model = Review # not instantiated 
    context_object_name = "reviews" # to rename object so the output will dynamically generate on server.

   
# using the TemplateView as a detail capture mechanism
# class SingleReviewView(TemplateView):
#    template_name = "reviews/single_review.html"

#    def get_context_data(self, **kwargs):
#          context = super().get_context_data(**kwargs)
#          review_id = kwargs["id"]
#          select_review = Review.objects.get(pk=review_id)
#          context["review"]= select_review
#          return context

# using the DetailView as a detail capture mechanism
class SingleReviewView(DetailView):
   """
   Simpler than above approach
   """
   template_name = "reviews/single_review.html"
   model = Review # note django uses the pk as the slug input in the urls.py

class AddFavouriteView(View):
    def post(self,request):
        review_id = request.POST["review_id"]
        fav_review = Review.objects.get(pk=review_id)
        request.session["favorite_review"] = fav_review # storing the fav_rev object in a dict with the key "favorite_review"
        return HttpResponseRedirect("/reviews/" + review_id)
  
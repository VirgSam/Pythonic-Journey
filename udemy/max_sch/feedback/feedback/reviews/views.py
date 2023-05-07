from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewFORM
from django.views import View
from .models import Review
from django.views.generic.base import TemplateView
from django.views.generic import ListView

# Create your views here.
class ReviewView(View):
   """
   Views as classes
   """
   def get(self,request):
      form = ReviewFORM()
      return render(request,"reviews/review.html",{"form":form})
   
   def post(self,request):
      form = ReviewFORM(request.POST)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect("/thank-you")
      return render(request,"reviews/review.html",{"form":form})
   

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
    template_name = "reviews/review_list.html"
    model = Review # not instantiated 
    context_object_name = "review"

    
    

    


class SingleReviewView(TemplateView):
   template_name = "reviews/single_review.html"

   def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         review_id = kwargs["id"]
         select_review = Review.objects.get(pk=review_id)
         context["review"]= select_review
         return context
   
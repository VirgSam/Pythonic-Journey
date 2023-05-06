from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewFORM
from django.views import View
#from .models import Review
from django.views.generic.base import TemplateView

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

# tried using the TemplateView
# class ThankYou(TemplateView):
#    template_name = "thank_you.html"
   
#    def thank_you(self, request):
#       return render(request,"reviews/thank_you.html")

class ThankYouView(View):
   """
   Thank you View in class representation
   """
   def get(self, request):
      return render(request,"reviews/thank_you.html")

   
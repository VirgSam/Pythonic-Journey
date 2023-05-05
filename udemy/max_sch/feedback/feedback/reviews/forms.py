from django import forms
from . models import Review

# class ReviewFORM(forms.Form):
#     user_name=forms.CharField(label="Your Name",required=True, max_length=100, error_messages={
                                            
#     "required":"Your Name Must Not Be Empty",
#     "max_length":"Please enter a shorter name!",

#     })# required true is always default, so no need to add it.

#     review =forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     ratings =forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

# another alternative to forms in django

class ReviewFORM(forms.ModelForm):
    class Meta:
        model = Review
        #fields = ['user_name','review','ratings']
        fields ='__all__'  # means select all fields in model and tranfer them over here
        # exclude = ['Field name you want to exclude']
        labels = {
            "user_name":"Your Name",
            "review": "Your Feedback",
            "ratings":"Your Rating", 
                  }
        error_messages = {
            "user_name":{
                "required":"Your Name Must Not Be Empty",
                "max_length":"Please enter a shorter name!"
                }
                  }
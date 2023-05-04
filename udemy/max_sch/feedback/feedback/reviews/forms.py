from django import forms

class ReviewFORM(forms.Form):
    user_name=forms.CharField(label="Your Name")
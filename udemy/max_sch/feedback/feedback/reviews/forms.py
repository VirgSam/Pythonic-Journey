from django import forms

class ReviewFORM(forms.Form):
    user_name=forms.CharField(label="Your Name",required=True, max_length=100, error_messages={
                                            
    "required":"Your Name Must Not Be Empty",
    "max_length":"Please enter a shorter name!",

    })# required true is always default, so no need to add it.
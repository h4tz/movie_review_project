from django import forms 
from .models import Review
from django.forms import ModelForm

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating' : forms.NumberInput(attrs={'min':1, 'max':5}),
            'comment' : forms.Textarea(attrs = {'rows': 4})
        }
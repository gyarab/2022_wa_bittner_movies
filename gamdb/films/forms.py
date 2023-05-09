from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class CommentForm(forms.Form):
    author = forms.CharField(required=False)
    text = forms.CharField(
        required=False, 
        widget=forms.Textarea(
            attrs=(
                'rows':3, 
                'class':'form-control'
                )
        )
        )
    rating = forms.IntegerField(
        required=False, 
        validators=[
            MinValueValidator(1), MaxValueValidator(100)
            ]
        widget=forms.NumberImput(
            attrs=(
                'class':'form-control'
            )
        )
        )

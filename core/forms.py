from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Add Review"}))
    class Meta:
        model = Review
        fields = ['comment']
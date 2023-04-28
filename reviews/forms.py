from django import forms
from .models import Review

class ReivewForm(forms.ModelForm):
    class Meta:
        model : Review
        fields = ('title', 'content',)
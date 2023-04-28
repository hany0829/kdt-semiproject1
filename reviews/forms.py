from django import forms
from .models import Review, Comment

class ReivewForm(forms.ModelForm):
    class Meta:
        model : Review
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):
    class Meta:
        model : Comment
        fields = ('content')
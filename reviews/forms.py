from django import forms
from .models import Review, Comment

class ReivewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], widget=forms.RadioSelect())
    class Meta:
        model = Review
        fields = ('title', 'content', 'image','rating',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
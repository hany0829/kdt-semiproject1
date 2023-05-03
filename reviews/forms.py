from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')], widget=forms.RadioSelect(), required=False)
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
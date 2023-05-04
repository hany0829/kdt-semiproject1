from django import forms
from .models import Review, Comment

class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label = '',
        widget=forms.TextInput(
            attrs= {
                'class' : 'write',
                'placeholder' : '제목을 입력해주세요.',
            }
        ),
        error_messages={'required' : ''},
    )
    content = forms.CharField(
        label = '',
        widget=forms.TextInput(
            attrs= {
                'class' : 'text',
                'placeholder' : '내용을 입력해주세요.',
            }
        ),
        error_messages={'required' : ''},
    )
    rating = forms.ChoiceField(choices=[(1, '⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (5, '⭐⭐⭐⭐⭐')], widget=forms.RadioSelect(
        attrs= {
            'class':'rating-horizontal'
        }
    ), required=False, label = '',)
    class Meta:
        model = Review
        fields = ('title', 'content', 'rating',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        
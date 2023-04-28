from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class CustomAuthentication(AuthenticationForm):
    username = forms.CharField(
        label = '아이디',
        widget = forms.TextInput(attrs={'class':'form-control',}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control',}),
    )

    class Meta:
        model = get_user_model
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'name', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
            'email': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
            'name': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'name')

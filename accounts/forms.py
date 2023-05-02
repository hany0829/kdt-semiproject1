from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm


class CustomAuthentication(AuthenticationForm):
    username = forms.CharField(
        label = 'ID',
        widget = forms.TextInput(attrs={'class':'form-control',}),
    )
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'class':'form-control',}),
    )

    class Meta:
        model = get_user_model
        fields = ('username','password')


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'password1', 'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
            'email': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
            'first_name': forms.TextInput(attrs={'class':'form-control custom-input-form',}),
        }


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'email', )

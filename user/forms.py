from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        "hx-post": "/check_username/",
        "hx-trigger": "keyup",
        # "hx-trigger": "every 1s",
        "hx-target": "#username-error",
        "class": "py-3 ps-4 font_fv font_style_b fw-lighter"
    }))

    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        "class": "py-3 ps-4 font_fv font_style_b fw-lighter",
    }))


class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        "class": "py-3 ps-4 font_fv font_style_b fw-lighter",
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Username',
                "class": "py-3 ps-4 font_fv font_style_b fw-lighter",
            }) ,
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                "class": "py-3 ps-4 font_fv font_style_b fw-lighter",
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Password',
                "class": "py-3 ps-4 font_fv font_style_b fw-lighter",
            }),

        }

    def clean_confirm_password(self):
        if self.cleaned_data['confirm_password'] != self.cleaned_data['password']:
            raise ValidationError('Parollar bir xil emas!!!')
        return self.cleaned_data['confirm_password']

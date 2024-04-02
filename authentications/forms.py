from django import forms
from .models import User
from datetime import datetime
from django.contrib.auth.password_validation import validate_password


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter password'}))
    date_of_birth = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD', 'class': 'form-control'}),
        input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
    )

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)  # Basic validation
        return password

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email address is already in use. Please use a different email.")
        return email

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'date_of_birth']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            # You can add more widgets for other fields here as needed
        }

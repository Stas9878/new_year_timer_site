from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя',widget=forms.TextInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Введите никнейм'}), )
    email = forms.EmailField(label='Почта',
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Введите ваш E-Mail'}))
    password1 = forms.CharField(max_length=50,label='Пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Пароль'}))
    password2 = forms.CharField(max_length=50,label='Подтвердите пароль', widget=forms.PasswordInput(
        attrs={"class": "form-control mb-1", 'placeholder': 'Подтверждение пароля'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Введите никнейм'}))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={"class": "form-control mb-1", 'placeholder': 'Пароль'}))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
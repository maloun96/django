from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Product, Subcategory


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


    name = forms.CharField(
        error_messages={'required': 'Introduceti numele'},
        label='Name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    price = forms.FloatField(
        error_messages={'required': 'Introduceti pretul', 'invalid': 'Valoarea trebuie sa fie numerica'},
        label='Price',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    subcategory = forms.ModelChoiceField(
        error_messages={'required': 'Selectati subcategoria'},
        label='Subcategory',
        queryset=Subcategory.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    image = forms.ImageField(
        error_messages={'required': 'Selectati imaginea'},
        label='Image',
        widget=forms.FileInput(attrs={'class': 'form-control'})
    )

class UserRegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))

class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control'}))


from django.contrib.auth.forms import UserCreationForm
from django import forms
type=(
    ('Doctor','Doctor'),
    ('Patient','Patient')
)


class Registerform(UserCreationForm):
    first_name=forms.CharField(max_length=200)
    last_name=forms.CharField(max_length=200)
    email=forms.EmailField()
    
    address=forms.CharField(max_length=200)
    city=forms.CharField(max_length=200)
    state=forms.CharField(max_length=200)
    pincode=forms.CharField(max_length=200)
    user_type=forms.ChoiceField(choices=type)

    
from django.forms import ModelForm
from .models import Tourist


from django import forms
from .models import *
class BookCreate(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class TouristForm(ModelForm):
    class Meta:
        model=Tourist
        fields='__all__'



from django import forms
from django.core.exceptions import ValidationError
from . import models

class AddPostForm(forms.Form):
    name = forms.CharField(min_length=5, label="Name",error_messages={"min_length": "Too short", "required": "cannot be empty"})
    Surname = forms.CharField(min_length=3, label="Surname")
    age = forms.IntegerField(label="Age")
    Address=forms.CharField(max_length=18)
    Email = forms.CharField(min_length=10, label="Email")
    Password = forms.CharField(max_length=8, label="Password")
    is_published = forms.BooleanField(initial=True, label="Remember Password")


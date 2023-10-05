from django.forms import forms
from .models import *

class MakeWIshForm(forms.ModelForm):
    model = Wish
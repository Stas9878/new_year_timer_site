from django import forms
from .models import *

class MakeWIshForm(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ('wish','author')
        widgets = {'wish': forms.Textarea(attrs={
            'class': 'textform',
            'id': 'wish',
            'placeholder': 'Например: "Хочу робота-паука"',
            'required':'true',
            'onkeyup':'checkParams()',            
        })}


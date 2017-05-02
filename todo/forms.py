import datetime
from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(label='Title:', max_length=100)
    text = forms.CharField(label='Text:', widget=forms.Textarea)

from django import forms
from django import forms

class FileForm(forms.Form):
    file = forms.FileField()
    
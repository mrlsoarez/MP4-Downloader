from django import forms

class NameForm(forms.Form):
    link = forms.CharField(label="Link", max_length=100)
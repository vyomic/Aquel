from django import forms


class NameForm(forms.Form):
    your_name = forms.CharField(label="fname", max_length=100)
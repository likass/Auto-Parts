from django import forms


class ContactFormEmail(forms.Form):
    name = forms.CharField(required=True, max_length=15, label='Name:')
    email = forms.EmailField(required=True, label='Email:')
    number = forms.CharField(required=True, max_length=20, label='Phone Number:')
    message = forms.CharField(required=True, max_length=100, widget=forms.Textarea, label='Message:')

from django import forms
from datetime import datetime



class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    dob = forms.DateField()
    gender = forms.CharField()
    organization = forms.CharField()
    
class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

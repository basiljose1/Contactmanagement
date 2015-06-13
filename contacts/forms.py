from django import forms
from datetime import datetime
#from django.core.mail import send_mail, BadHeaderError
from .models import Group



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

class EmailForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    pass_word = forms.CharField(max_length=32, widget=forms.PasswordInput)
    topic = forms.CharField()
    c=0
    CHOICES=[]
    while (c<Group.objects.all().count()):
       a=Group.objects.all()[c]
       c=c+1
       CHOICES +=[
        [a, a],
         ]
    group_name = forms.ChoiceField(choices=CHOICES, required=True, label='Group Name',widget=forms.Select(attrs={'width': 30}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 10,'cols': 60}))
    


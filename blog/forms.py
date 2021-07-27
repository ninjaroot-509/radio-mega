from django import forms
from django.contrib.auth.models import User

from .models import Comment, Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'sujet', 'body']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'body')
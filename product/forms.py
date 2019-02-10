from django import forms
from django.contrib.auth.models import User


class ContactForm(forms.Form):
	contact_name  = forms.CharField(required=True)
	contact_mail  = forms.EmailField(required=True)
	content = forms.CharField(required=True,widget=forms.Textarea)
	




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

from django import forms
from contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ()
        widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control'}),
          'email': forms.TextInput(attrs={'class': 'form-control'}),
          'message': forms.Textarea(attrs={'class': 'form-control'})
        }
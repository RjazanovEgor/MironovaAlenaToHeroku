# sendemail/forms.py
from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Email', required=True)
    name = forms.CharField(label='Имя', required=True)
    phone = forms.CharField(label='Телефон', required=True)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea, required=True)

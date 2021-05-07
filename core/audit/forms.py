from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Audit, Exploit


class AddNewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1','password2']


class AuditForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = '__all__'
        widgets = {
            'author' : forms.HiddenInput,
        }

class ExploitForm(forms.ModelForm):
    class Meta():
        model = Exploit
        fields = '__all__'

    def clean(self):
        for field in self.fields:
            self.cleaned_data[field]

        return self.cleaned_data

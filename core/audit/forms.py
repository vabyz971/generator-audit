from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import Audit, Exploit


class AddNewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : widgets.TextInput(attrs={'class' : 'form-control'}),
            'email' : widgets.EmailInput(attrs={'class' : 'form-control'}),
            'password1' : widgets.PasswordInput(attrs={'class' : 'form-control'}),
            'password2' : widgets.PasswordInput(attrs={'class' : 'form-control'},),
        }


class AuditForm(forms.ModelForm):
    class Meta:
        model = Audit
        fields = ('name', 'readers')


class ExploitForm(forms.ModelForm):
    class Meta():
        model = Exploit
        fields = '__all__'

    def clean(self):
        for field in self.fields:
            self.cleaned_data[field]

        return self.cleaned_data

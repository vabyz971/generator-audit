from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms import widgets
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, ButtonHolder, Submit
from .custom_layout_object import *

from .models import Audit, Exploit


class AddNewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': widgets.TextInput(attrs={'class': 'form-control'}),
            'email': widgets.EmailInput(attrs={'class': 'form-control'}),
            'password1': widgets.PasswordInput(attrs={'class': 'form-control'}),
            'password2': widgets.PasswordInput(attrs={'class': 'form-control'},),
        }


class AuditForm(forms.ModelForm):

    class Meta:
        model = Audit
        exclude = ['author', ]

    def __init__(self, *args, **kwargs):
        super(AuditForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'mb-3 col-auto'
        self.helper.label_class = 'form-label'
        self.helper.field_class = 'form-control'
        self.helper.layout = Layout(
            Div(
                Field('name'),
                Field('readers'),
                Fieldset('Exploits',
                         Formset('exploits')),
                ButtonHolder(Submit('submit', 'valider')),
            )
        )


class ExploitForm(forms.ModelForm):

    class Meta():
        model = Exploit
        exclude = ()


ExploitFormSet = forms.inlineformset_factory(Audit, Exploit,
                                             form=ExploitForm,
                                             fields=['description','image', 'level_critical'],
                                             extra=2, can_delete=True)

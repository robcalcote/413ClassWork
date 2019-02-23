from django import forms
from django.core.exceptions import ValidationError
# This allows the Validation Errors to translate to other languages/frameworks later
from django.utils.translation import ugettext_lazy as _

from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):

    context = {
       
    }
    
    return request.dmp.render('login.html', context)

class LoginForm(forms.Form):
    username = forms.TextInput(help_text="Enter login username")
    password = forms.PasswordInput(help_text="Enter password")

    def clean_username(self):
        data = self.cleaned_data['username']

        # Check if username is valid
        if data == '':
            raise ValidationError(_('Invalid username - please enter a value'))

        # Return the cleaned data.
        return data
    
    def clean_password(self):
        data = self.cleaned_data['password']

        # Check if username is valid
        if data == '':
            raise ValidationError(_('Invalid password - please enter a value'))

        # Return the cleaned data.
        return data

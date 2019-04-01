from django import forms
from django.contrib.auth import authenticate, login
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect

from django.conf import settings
from django_mako_plus import view_function, jscontext

@view_function
def process_request(request):
    
    # Process the form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password = form.cleaned_data.get('password'))
            login(request, user)
            return HttpResponseRedirect('/')
    else: # GET
        form = LoginForm()

    # render the template
    return request.dmp.render('login.html', {
        'form': form, 
    })

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    # Runs a bundle clean on both username and password
    def clean(self):
        user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
        if user is None:
            raise forms.ValidationError('Invalid username or password')
        return self.cleaned_data

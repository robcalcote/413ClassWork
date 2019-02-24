from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django_mako_plus import view_function


@view_function
def process_request(request):
    # log the user out
    logout(request)
    # redirect to login page
    return HttpResponseRedirect('/account/login/')
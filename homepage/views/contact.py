from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone

@view_function
def process_request(request):
    # did the user submit?
    if request.method == "POST":
        # check all the variables
        # we assume the user does it all wrong
        print(request.POST['yourname'])

        #if user did it right:
        # do the work (reset password, create account, finalize sale, etc)
        return HttpResponseRedirect('/somewhere/else/')

    context = {

    }

    return request.dmp.render('contact.html', context)
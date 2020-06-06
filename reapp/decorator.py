from reapp.models import Employee
from django.shortcuts import redirect
import logging



def is_authenticated(f):
    def wrap(request, *args, **kwargs):
        # this check the session if userid key exist, if not it will redirect to login page
        try:
            user_obj = Employee.objects.get(id=request.session['pk'])
        except:
            user_obj = False
        if 'pk' in request.session.keys() and user_obj:
            return f(request, *args, **kwargs)
        request.session.clear()
        return redirect("login")
    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


logger = logging.getLogger(__name__)

def if_logged(f):
    def helper(request,*args,**kwargs):
        try:
            return f(request,*args,**kwargs)
        except Exception as e:
            return logger.error(e)
    helper.__doc__ = f.__doc__
    helper.__name__ = f.__name__
    return helper

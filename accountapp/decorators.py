from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(requsest, *args, **kwargs):
        target_user = User.objects.get(pk=kwargs['pk'])
        if target_user ==requsest.user:
            return func(requsest, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated
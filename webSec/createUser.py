from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)
def create_user(request):
    # user = User.objects.create_user('stolas', password='stolas_pw')
    # user.first_name = 'Stolas'
    # user.save()
    # user = User.objects.create_user('blitzo', password='blitzo_pw')
    # user.first_name = 'Blitzo'
    # user.last_name = 'Buckzo'
    # user.save()
    # user = User.objects.create_user('alastor', password='alastor_pw')
    # user.first_name = 'Alastor'
    # user.save()
    # user = User.objects.create_user('angle', password='angle_pw')
    # user.first_name = 'Anthony'
    # user.save()
    return redirect('/admin/auth/user/')
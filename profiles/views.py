from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.views import generic, View


# Create your views here.


def my_profile(request):
    """ RENDER THE PROFILE FUNCTION AND GIVE ACCESS TO THE FORM """
    """WHERE CAN ENTER/UPDATE IT """
    """ THE PROFILE IS CREATED BY SIGNAL, SO DOESNT HAVE ANYOTHER """
    """ INFORMATION THAN THE USER """
    user_obj = get_object_or_404(UserProfile, user=request.user)

    return render(request, 'user_profile.html', {'user': user_obj, })

from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from .forms import ProfileForm
from django.views import generic, View
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def my_profile(request):
    """ RENDER THE PROFILE FUNCTION AND GIVE ACCESS TO THE FORM """
    """WHERE CAN ENTER/UPDATE IT """
    """ THE PROFILE IS CREATED BY SIGNAL, SO DOESNT HAVE ANYOTHER """
    """ INFORMATION THAN THE USER """
    user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile had been updated successfully!')
        else:
            form = ProfileForm(instance=user)
    return render(request, 'profiles/user_profile.html', {'form': form,
                  'user': user, })

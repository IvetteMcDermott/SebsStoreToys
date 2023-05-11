from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from sts_store.models import Ware
from profiles.models import UserProfile
from .models import Bookmarks



# Create your views here.


@login_required
def bookmarks(request, *args, **kwargs):
    """ VIEW FOR USER INTERESTS """
    user = UserProfile.objects.get(user=request.user)
    template = 'bookmarks/user_bookmarks.html'
    bookmarks = Bookmarks.objects.filter(user=user)
    context = {
        'wares': bookmarks,
    }
    return render(request, template, context)


@login_required
def toggle_bookmark(request, ware_id):
    """ BOOKMARK TOGGLE IF ADD OR REMOVE """

    if request.method == 'POST':

        user = UserProfile.objects.get(user=request.user)
        ware = get_object_or_404(Ware, id=ware_id)
        bookmark = Bookmarks.objects.filter(user=user, ware=ware).exists()

        if bookmark:
            bookmark_ware = Bookmarks.objects.get(
                user=user,
                ware=ware,
            )
            bookmark_ware.delete()

            # messages.remove
        else:
            bookmark_ware = Bookmarks.objects.create(
                user=user,
                ware=ware,
            )
            # messages.success

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

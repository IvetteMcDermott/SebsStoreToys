from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from sts_store.models import Ware
from profiles.models import UserProfile
from .models import Bookmarks
from django.contrib import messages


# Create your views here.


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
            messages.success(request, 'Bookmark had been removed successfully')
        else:
            bookmark_ware = Bookmarks.objects.create(
                user=user,
                ware=ware,
            )
            messages.success(request, 'The ware had been bookmarked successfully')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

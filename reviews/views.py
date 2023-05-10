from django.shortcuts import render, get_object_or_404
from .models import Review
from .forms import ReviewForm
from sts_store.models import Ware
from django.views import generic, View
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.http import HttpResponse


# Create your views here.


@login_required
def add_review(request):
    """ GIVE ACCESS TO THE FORM """
    """ WHERE CAN ENTER A REVIEW """

    ware = get_object_or_404(Ware, user=request.user)
    template = 'sts_store/ware_details.html'

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile had been updated successfully!')
    else:
        form = ReviewForm(instance=user)

    context = {
                'form': form,
                'user': user,
                'ware': ware,
                }

    return render(request, template, context)

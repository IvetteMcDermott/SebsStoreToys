from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from bookmarks.models import Bookmarks
from .forms import ProfileForm
from checkout.models import Order
from django.views import generic, View
from django.views.generic import CreateView

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.http import HttpResponse


# Create your views here.


@login_required
def my_profile(request):
    """ RENDER THE PROFILE FUNCTION AND GIVE ACCESS TO THE FORM """
    """WHERE CAN ENTER/UPDATE IT """
    """ THE PROFILE IS CREATED BY SIGNAL, SO DOESNT HAVE ANYOTHER """
    """ INFORMATION THAN THE USER """
    user = get_object_or_404(UserProfile, user=request.user)
    orders = user.orders.all().order_by('-date')[:5]
    template = 'profiles/user_profile.html'
    bookmarks = Bookmarks.objects.filter(user=user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Profile had been updated successfully!')
            form = ProfileForm()
    else:
        form = ProfileForm(instance=user)

    context = {
                'form': form,
                'user': user,
                'orders': orders,
                'bookmarks': bookmarks,
                }

    return render(request, template, context)


class OrderDetail(CreateView):
    """
    RENDER THE DETAILS PAGE OF THE SELECTED WARE
    """
    model = Order

    def get(self, request, order_number, *args, **kwargs):
        model = Order
        queryset = model.objects.all()
        order = get_object_or_404(queryset, order_number=order_number)

        return render(
            request,
            "profiles/order_details.html",
            {
               "order": order,
            },
        )

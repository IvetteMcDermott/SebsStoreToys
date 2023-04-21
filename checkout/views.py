from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from .forms import OrderForm

import stripe


def checkout(request):
    cart = request.session.get('cart', {})
    order_form = OrderForm()
    context = {
        'order_form': order_form,
        'cart': cart,
    }

    return render(request, 'checkout/checkout.html', context)

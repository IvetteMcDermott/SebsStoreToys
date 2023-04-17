from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import HttpResponseRedirect

from sts_store.models import Ware, WareImage


def view_cart(request):
    """ A view that renders the shopping cart contents page """

    return render(request, 'cart/shopping_cart.html')


def add_to_cart(request, ware_id):
    """ Add the specified ware to the shopping cart """

    ware = get_object_or_404(Ware, pk=ware_id)
    quantity = int(request.POST.get('quantity'))
    # redirect_url = request.POST.get('redirect_url')

    cart = request.session.get('cart', {})

    if ware_id in list(cart.keys()):
        cart[ware_id] += quantity
            # messages.success(request,
            #                  (f'Updated {product.name} '
            #                   f'quantity to {bag[item_id]}'))
    else:
        cart[ware_id] = quantity
            # messages.success(request, f'Added {product.name} to your bag')

    request.session['cart'] = cart
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def remove_from_cart(request, ware_id):
    """Remove the item from the shopping bag"""

    try:
        ware = get_object_or_404(Ware, pk=ware_id)
        cart = request.session.get('cart', {})
        
        cart.pop(ware_id)
            # messages.success(request, f'Removed {product.name} from your bag')

        request.session['cart'] = cart
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

    except Exception as e:
        # messages.error(request, f'Error removing item: {e}')
        return HttpResponseRedirect(request.META['HTTP_REFERER'])

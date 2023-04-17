from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from sts_store.models import Ware, WareImage


def cart_content(request):

    cart_wares = []
    total = 0
    wares_count = 0
    cart = request.session.get('cart', {})

    for ware_id, quantity in cart.items():
        if isinstance(quantity, int):
            ware = get_object_or_404(Ware, pk=ware_id)
            total += quantity * ware.price
            wares_count += quantity
            cart_wares.append({
                'ware_id': ware_id,
                'quantity': quantity,
                'ware': ware,
            })
        else:
            ware = get_object_or_404(Ware, pk=ware_id)

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'cart_wares': cart_wares,
        'total': total,
        'ware_count': wares_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context

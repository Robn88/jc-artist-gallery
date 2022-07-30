from django.conf import settings
from django.shortcuts import get_object_or_404
from artwork.models import Artwork


def bag_contents(request):

    bag_items = []
    total = 0
    artwork_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        artwork = get_object_or_404(Artwork, pk=item_id)
        total += quantity * artwork.price
        artwork_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'artwork': artwork
        })

    grand_total = total + 99

    context = {
        'bag_items': bag_items,
        'total': total,
        'artwork_count': artwork_count,
        'grand_total': grand_total
    }

    return context

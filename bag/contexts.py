from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    artwork_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'artwork_count': artwork_count,
    }

    return context

from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages

from artwork.models import Artwork

# Create your views here.


def view_bag(request):
    """ A view to return the bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, artwork_id):
    """ Add the requested piece of work to the bag """
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[artwork_id] = 1

    request.session['bag'] = bag

    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """Remove the artwork from the shopping bag"""

    try:
        artwork = get_object_or_404(Artwork, pk=item_id)
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        messages.success(request, f'Removed {artwork.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

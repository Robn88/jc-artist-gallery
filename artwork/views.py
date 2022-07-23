from django.shortcuts import render, get_object_or_404
from .models import Artwork
from bag.contexts import bag_contents

from .forms import ArtworkForm

# Create your views here.


def all_artwork(request):
    """ A view to return all of the artwork, including sorting and search queries """

    artwork = Artwork.objects.all()

    context = {
        'artwork': artwork,
    }

    return render(request, 'artwork/artwork.html', context)


def artwork_detail(request, artwork_id):
    """ A view to return an individual piece of artwork """

    piece = get_object_or_404(Artwork, pk=artwork_id)
    bag = request.session.get('bag', {})
    already_in_bag = False

    for item in bag:
        if int(item) == piece.id:
            already_in_bag = True
        else:
            already_in_bag = False

    context = {
        'piece': piece,
        'already_in_bag': already_in_bag,
    }

    return render(request, 'artwork/artwork_detail.html', context)


def add_artwork(request):
    """ Add artwork to the store """
    form = ArtworkForm
    template = 'artwork/add_artwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

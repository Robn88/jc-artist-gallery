from django.shortcuts import render, get_object_or_404
from .models import Artwork

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
    print(piece, artwork_id)

    context = {
        'piece': piece,
    }

    return render(request, 'artwork/artwork_detail.html', context)

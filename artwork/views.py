from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Artwork
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from bag.contexts import bag_contents

from .forms import ArtworkForm


def all_artwork(request):
    # A view to return all of the artwork,
    # including sorting and search queries

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


@login_required
def add_artwork(request):
    """ Add artwork to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added artwork!')
            return redirect(reverse('add_artwork'))
        else:
            messages.error(request, 'Failed to add artwork. Please ensure \
                 the form is valid.')
    else:
        form = ArtworkForm()
    template = 'artwork/add_artwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

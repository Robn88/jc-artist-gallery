from django.shortcuts import render, redirect

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
    print(request.session['bag'])
    print(artwork_id)

    return redirect(redirect_url)

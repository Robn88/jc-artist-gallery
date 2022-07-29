from django.shortcuts import render
from django.contrib import messages

from .forms import ContactForm
from .models import ContactMessage


def contact_form(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'message')
    else:
        form = ContactForm()

    template = 'contact/contact.html'

    context = {
        'form': form,
    }

    return render(request, template, context)

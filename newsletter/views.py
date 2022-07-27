from django.shortcuts import render
from django.contrib import messages

from .forms import NewsletterForm
from .models import NewsletterReceiver


def newsletter_signup(request):

    form = NewsletterForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterReceiver.objects.filter(email=instance.email).exists():
            messages.error(request, 'Sorry, this email address is already \
                            signed up to the newsletter!')
        else:
            instance.save()

    template = 'newsletter/newsletter.html'

    context = {
        'form': form,
    }

    return render(request, template, context)

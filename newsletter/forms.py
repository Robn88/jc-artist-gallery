from django import forms
from .models import NewsletterReceiver


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterReceiver
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return Email

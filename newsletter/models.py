from django.db import models


class NewsletterReceiver(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

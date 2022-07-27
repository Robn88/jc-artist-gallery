from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=50, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

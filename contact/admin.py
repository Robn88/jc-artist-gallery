from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'message',
        'date_created'
    )


admin.site.register(ContactMessage, ContactMessageAdmin)

from django.contrib import admin
from .models import NewsletterReceiver


class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'date_created'
    )


admin.site.register(NewsletterReceiver, NewsletterAdmin)

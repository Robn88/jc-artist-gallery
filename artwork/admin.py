from django.contrib import admin
from .models import Artwork, Category

# Register your models here.


class ArtworkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'technique',
        'dimensions',
        'is_framed',
        'price',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Artwork, ArtworkAdmin)
admin.site.register(Category, CategoryAdmin)

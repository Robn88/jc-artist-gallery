from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Artwork(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    technique = models.CharField(max_length=254, null=False, blank=False)
    name = models.CharField(max_length=254, null=False, blank=False)
    dimensions = models.CharField(max_length=254, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    is_framed = models.BooleanField(default=False, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=False, blank=False)
    artist = models.CharField(max_length=254, null=True, blank=True)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    price_framed = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

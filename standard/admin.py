from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Product)
admin.site.register(models.News)
admin.site.register(models.Location)
admin.site.register(models.Cart)
admin.site.register(models.Vendor)
admin.site.register(models.ShopLocation)

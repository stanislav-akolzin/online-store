from django.contrib import admin
from . import models


admin.site.register(models.ItemCategory)
admin.site.register(models.Item)
admin.site.register(models.ItemChange)
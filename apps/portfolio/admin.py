from django.contrib import admin
from apps.portfolio.models import Photos


@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    pass


from django.contrib import admin
from apps.portfolio.models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


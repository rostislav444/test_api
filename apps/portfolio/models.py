import uuid

from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone

from apps.portfolio.abstract.fields import CustomImageField


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (('user', 'name',),)


class Photos(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="photos")
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = CustomImageField(upload_to='photos/')
    image_path = models.CharField(max_length=1024, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now, blank=True)

    class Meta:
        ordering = ('-created',)

    @property
    def get_slug(self):
        symbols = uuid.uuid4().hex[0:8]
        values = [self.portfolio.name, self.name, symbols]
        return slugify('-'.join(values))


class Comments(models.Model):
    photo = models.ForeignKey(Photos, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    text = models.TextField()

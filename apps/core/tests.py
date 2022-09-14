from django.test import override_settings
from django.urls import path, include
from faker import Faker
from rest_framework.test import APITestCase, URLPatternsTestCase

from apps.user.factories import UserFactory
from project import settings
import os


TEST_MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'test_data')


@override_settings(MEDIA_ROOT=TEST_MEDIA_ROOT)
class BaseTestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('project.urls')),
    ]

    def setUp(self):
        self.faker = Faker()
        self.user = UserFactory.create()
        self.client.force_authenticate(user=self.user)
        self.login_data = {
            "username": self.user.username,
            "password": "test"
        }

    def tearDown(self):
        for root, dirs, files in os.walk(TEST_MEDIA_ROOT, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        try:
            os.rmdir(TEST_MEDIA_ROOT)
        except FileNotFoundError:
            pass

from django.urls import path, include, reverse
from faker import Faker
from rest_framework.test import APITestCase, URLPatternsTestCase

from apps.user.factories import UserFactory

faker = Faker()


class PortfolioTestCase(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('', include('project.urls')),
    ]

    def setUp(self):
        self.user = UserFactory.create()
        self.client.force_authenticate(user=self.user)
        self.login_data = {
            "username": self.user.username,
            "password": "test"
        }

    def test_login(self):
        endpoint = reverse('user:login')
        response = self.client.post(endpoint, data=self.login_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        endpoint = reverse('user:register-list')
        data = {
            'username': faker.email(),
            'email': faker.email(),
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'password': 'Pineapple1234',
            'password2': 'Pineapple1234',
        }
        response = self.client.post(endpoint, data=data, format='json')
        self.assertEqual(response.status_code, 201)

    def test_logout(self):
        endpoint = reverse('user:logout')
        login_response = self.client.post(reverse('user:login'), data=self.login_data, format='json')
        logout_response = self.client.post(endpoint, data=login_response.data, format='json')
        self.assertEqual(logout_response.status_code, 205)




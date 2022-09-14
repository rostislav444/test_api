from django.urls import reverse

from apps.core.tests import BaseTestCase
from apps.user.factories import UserFactory


class UserTestCase(BaseTestCase):
    def test_login(self):
        endpoint = reverse('user:login')
        response = self.client.post(endpoint, data=self.login_data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_registration(self):
        endpoint = reverse('user:register-list')
        data = {
            'username': self.faker.email(),
            'email': self.faker.email(),
            'first_name': self.faker.first_name(),
            'last_name': self.faker.last_name(),
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

    def test_profile_update(self):
        endpoint = reverse('user:profile-detail', kwargs={'pk': self.user.pk})
        response = self.client.patch(endpoint, data={'name': 'test_name'}, format='json')
        self.assertEqual(response.status_code, 200)

    def test_profile_delete(self):
        endpoint = reverse('user:profile-detail', kwargs={'pk': self.user.pk})
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)






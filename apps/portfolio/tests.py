from django.urls import reverse
from faker import Faker

from apps.core.tests import BaseTestCase
from apps.portfolio.factories import PortfolioFactory, PhotoFactory
from project import settings

faker = Faker()


class PortfolioTestCase(BaseTestCase):
    def test_portfolio_create(self):
        endpoint = reverse('portfolio:portfolio-list')
        data = {
            'name': faker.text(max_nb_chars=5),
            'description': faker.text(max_nb_chars=40),
        }
        response = self.client.post(endpoint, data)
        self.assertEqual(response.status_code, 201)

    def test_portfolio_update(self):
        portfolio = PortfolioFactory.create(user=self.user)
        endpoint = reverse('portfolio:portfolio-detail', kwargs={'pk': portfolio.pk})
        response = self.client.patch(endpoint, data={'name': 'test_name'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test_name')

    def test_portfolio_delete(self):
        portfolio = PortfolioFactory.create(user=self.user)
        endpoint = reverse('portfolio:portfolio-detail', kwargs={'pk': portfolio.pk})
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)

    def test_photo_create(self):
        endpoint = reverse('portfolio:photo-list')
        portfolio = PortfolioFactory.create(user=self.user)
        filename = 'test.jpeg'
        with open(settings.STATICFILE_DIR + '/' + filename, 'rb') as f:
            data = {
                'portfolio_id': portfolio.id,
                'name': faker.text(max_nb_chars=5),
                'description': faker.text(max_nb_chars=40),
                'image': f
            }
            response = self.client.post(endpoint, data)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.data['image'].split('.')[1], filename.split('.')[1])

    def test_photo_get(self):
        endpoint = reverse('portfolio:photo-list')
        photo = PhotoFactory.create()
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['id'], photo.id)

    def test_photo_update(self):
        photo = PhotoFactory.create()
        endpoint = reverse('portfolio:photo-detail', kwargs={'pk': photo.pk})
        response = self.client.patch(endpoint, data={'name': 'test_name'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test_name')

    def test_photo_delete(self):
        photo = PhotoFactory.create()
        endpoint = reverse('portfolio:photo-detail', kwargs={'pk': photo.pk})
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)

    def test_photo_filter(self):
        endpoint = reverse('portfolio:photo-list')
        photo = PhotoFactory.create()

        # Filter name
        response = self.client.get(endpoint + f'?name={photo.name}')
        self.assertEqual(response.data[0]['name'], photo.name)

        # Filter description
        response = self.client.get(endpoint + f'?description={photo.description}')
        self.assertEqual(response.data[0]['description'], photo.description)

        # Filter portfolio name
        response = self.client.get(endpoint + f'?portfolio__name={photo.portfolio.name}')
        self.assertEqual(response.data[0]['portfolio'], photo.portfolio.name)

    def test_comment_creation(self):
        endpoint = reverse('portfolio:comment-list')
        photo = PhotoFactory.create()
        data = {'photo_id': photo.id, 'text': 'Amazing!'}
        response = self.client.post(endpoint, data)
        self.assertEqual(response.status_code, 201)










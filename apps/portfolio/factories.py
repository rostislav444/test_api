import factory
from faker import Faker

from apps.portfolio.models import Portfolio, Photo
from apps.user.factories import UserFactory
from project import settings

faker = Faker()


class PortfolioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Portfolio

    user = factory.SubFactory(UserFactory)
    name = faker.text(max_nb_chars=5)
    description = faker.text(max_nb_chars=40)


class PhotoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Photo

    portfolio = factory.SubFactory(PortfolioFactory)
    name = faker.text(max_nb_chars=5)
    description = faker.text(max_nb_chars=40)
    image = factory.django.FileField(filename=settings.STATICFILE_DIR + '/test.jpeg')


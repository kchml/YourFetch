import factory
from accounts.factories import UserFactory


class FeedFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'feeds.Feed'
        django_get_or_create = ('address', 'addressrss', 'user', 'x_path')

    address = 'https://test.com'
    addressrss = 'test'
    user = factory.SubFactory(UserFactory)
    x_path = '//test'


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'feeds.Item'
        django_get_or_create = (
            'title', 'description', 'feed',
            'image', 'directlink', 'slug', 'status')

    title = 'test'
    description = 'test'
    feed = factory.SubFactory(FeedFactory)
    image = 'https://test.com'
    directlink = 'https://test.com'
    slug = 'https://test.com'
    status = 0

import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'accounts.User'
        django_get_or_create = ('email', 'username', 'password')

    email = 'test_user@gmail.com'
    username = 'test_user'
    password = ''

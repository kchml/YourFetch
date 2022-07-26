from django.test import TestCase
from django.urls import reverse
from accounts.factories import UserFactory


class HomeViewTestCase(TestCase):

    def setUp(self):
        user = UserFactory()
        self.client.force_login(user)

    def test_home_response(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class LoginPageViewTestCase(TestCase):

    def test_login_page_response(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)


class LogoutUserViewTestCase(TestCase):

    def setUp(self):
        user = UserFactory()
        self.client.force_login(user)

    def test_logout_user_response(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_logout_user_redirect_location(self):
        response = self.client.get(
            reverse('logout'))
        location = response.headers['location']
        self.assertEqual(location, '/login/')


class RegisterPageViewTestCase(TestCase):

    def test_register_page_response(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

from django.test import Client
from django.test import TestCase
from django.urls import reverse
from feeds.factories import FeedFactory, UserFactory
from feeds.models import Feed


class AddSiteViewTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()
        self.client.force_login(self.user)

    def test_add_site_response(self):
        response = self.client.get(reverse('add_feed'))
        self.assertEqual(response.status_code, 200)

    def test_add_site_adding_site(self):
        data = {
            'address': 'https://test.com',
            'x_path': '//test',
            }
        client = Client()
        client.force_login(self.user)
        response = client.post('/addfeed/', data)
        self.assertEqual(response.status_code, 302)
        location = response.headers['location']
        self.assertEqual(location, '/')
        Feed.objects.get(**data)


class UserPageViewTestCase(TestCase):

    def setUp(self):
        user = UserFactory()
        self.client.force_login(user)

    def test_user_page_response(self):
        response = self.client.get(reverse('user_feeds'))
        self.assertEqual(response.status_code, 200)


class DeleteSiteViewTestCase(TestCase):

    def setUp(self):
        self.feed = FeedFactory()
        self.client.force_login(self.feed.user)

    def test_delete_site_response_by_name(self):
        response = self.client.get(
            reverse('delete_feed', args=[self.feed.id]))
        self.assertEqual(response.status_code, 302)

    def test_delete_site_redirect_location(self):
        response = self.client.get(
            reverse('delete_feed', args=[self.feed.id]))
        location = response.headers['location']
        self.assertEqual(location, '/')


class EditFeedViewTestCase(TestCase):

    def setUp(self):
        self.feed = FeedFactory()
        self.client.force_login(self.feed.user)

    def test_edit_feed_response(self):
        response = self.client.get(
            reverse('edit_feed', args=[self.feed.id]))
        self.assertEqual(response.status_code, 200)


class FeedItemsViewTestCase(TestCase):

    def setUp(self):
        user = UserFactory()
        self.feed = FeedFactory()
        self.client.force_login(user)

    def test_feed_items_response_by_name(self):
        response = self.client.get(
            reverse('feed_items', args=[self.feed.id]))
        self.assertEqual(response.status_code, 200)


class AllItemsViewTestCase(TestCase):

    def setUp(self):
        user = UserFactory()
        self.client.force_login(user)

    def test_all_items_view_response(self):
        self.client.login(
            email='testuser1@gmail.com',
            password='1X<ISRUkw+tuK'
        )
        response = self.client.get(reverse('all_items_list'))
        self.assertEqual(response.status_code, 200)


class OneItemViewTestCase(TestCase):

    def setUp(self):
        user = UserFactory()
        self.feed = FeedFactory()
        self.client.force_login(user)

    def test_one_item_view_response(self):
        response = self.client.get(
            reverse('one_item_list', args=[self.feed.id]))
        self.assertEqual(response.status_code, 200)

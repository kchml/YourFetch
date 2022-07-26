from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import home, login_page, logout_user, register_page
from feeds.views import user_page, add_site, delete_site, edit_feed
from feeds.views import get_feed_items, all_items_view, one_item_view


class TestUrls(TestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login_page)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout_user)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register_page)

    def test_user_page(self):
        url = reverse('user_feeds')
        self.assertEqual(resolve(url).func, user_page)

    def test_add_site(self):
        url = reverse('add_feed')
        self.assertEqual(resolve(url).func, add_site)

    def test_delete_feed(self):
        url = reverse('delete_feed', args=['1'])
        self.assertEqual(resolve(url).func, delete_site)

    def test_edit_feed(self):
        url = reverse('edit_feed', args=['1'])
        self.assertEqual(resolve(url).func, edit_feed)

    def test_get_feed_items(self):
        url = reverse('get_feed_items', args=['1'])
        self.assertEqual(resolve(url).func, get_feed_items)

    def test_feed_items(self):
        url = reverse('delete_feed', args=['1'])
        self.assertEqual(resolve(url).func, delete_site)

    def test_feed_screen(self):
        url = reverse('all_items_list')
        self.assertEqual(resolve(url).func, all_items_view)

    def test_one_feed_screen(self):
        url = reverse('one_item_list', args=['1'])
        self.assertEqual(resolve(url).func, one_item_view)

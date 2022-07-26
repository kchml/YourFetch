from django.test import TestCase
from feeds.forms import FeedForm
from feeds.models import Feed


class FeedFormTestCase(TestCase):

    def test_FeedForm(self):
        form = FeedForm(data={
            'address': 'https://test.com',
            'x_path': '//test',
        })
        self.assertTrue(form.is_valid())

    def test_FeedForm_address_label(self):
        form = FeedForm()
        self.assertTrue(
            form.fields['address'].label == ''
        )

    def test_FeedForm_x_path_label(self):
        form = FeedForm()
        self.assertTrue(
            form.fields['address'].label == ''
        )

    def test_FeedForm_Meta_model(self):
        form = FeedForm().Meta()
        self.assertTrue(form.model, Feed)

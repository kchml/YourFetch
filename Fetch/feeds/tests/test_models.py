from django.test import TestCase
from feeds.models import Feed, Item
from feeds.factories import FeedFactory, ItemFactory


class ModelFeedTest(TestCase):

    def setUp(self):
        self.feed = FeedFactory()

    def test_label_address_feed_label(self):
        feed = Feed.objects.get(id=self.feed.id)
        field_label = feed._meta.get_field('address').verbose_name
        self.assertEqual(field_label, 'address')

    def test_label_addressrss_feed(self):
        feed = Feed.objects.get(id=self.feed.id)
        field_label = feed._meta.get_field('addressrss').verbose_name
        self.assertEqual(field_label, 'addressrss')

    def test_label_user_feed(self):
        feed = Feed.objects.get(id=self.feed.id)
        field_label = feed._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_label_x_path_feed(self):
        feed = Feed.objects.get(id=self.feed.id)
        field_label = feed._meta.get_field('x_path').verbose_name
        self.assertEqual(field_label, 'x path')

    def test_max_length_address_feed(self):
        feed = Feed.objects.get(id=self.feed.id)
        max_length = feed._meta.get_field('address').max_length
        self.assertEqual(max_length, 400)

    def test_max_length_addressrss_feed(self):
        feed = Feed.objects.get(id=self.feed.id)
        max_length = feed._meta.get_field('addressrss').max_length
        self.assertEqual(max_length, 400)

    def test_max_length_x_path_feed(self):
        feed = Feed.objects.get(id=self.feed.id)
        max_length = feed._meta.get_field('x_path').max_length
        self.assertEqual(max_length, 300)

    def test_name_feed(self):
        feed = Feed.objects.get(id=self.feed.id)
        address_field = feed.address
        self.assertEqual(str(feed), address_field)


class ModelItemTest(TestCase):

    def setUp(self):
        self.item = ItemFactory()

    def test_auto_now_add_created_item(self):
        item = Item.objects.get(id=self.item.id)
        self.assertTrue(item.created)

    def test_auto_now_add_date_published_item(self):
        item = Item.objects.get(id=self.item.id)
        self.assertTrue(item.date_published)

    def test_label_created_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('created').verbose_name
        self.assertEqual(field_label, 'created')

    def test_label_date_published_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('date_published').verbose_name
        self.assertEqual(field_label, 'date published')

    def test_label_title_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_label_description_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_label_feed_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('feed').verbose_name
        self.assertEqual(field_label, 'feed')

    def test_label_image_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'image')

    def test_label_directlink_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('directlink').verbose_name
        self.assertEqual(field_label, 'directlink')

    def test_label_slug_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('slug').verbose_name
        self.assertEqual(field_label, 'slug')

    def test_label_status_item(self):
        item = Item.objects.get(id=self.item.id)
        field_label = item._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_editable_date_published_item(self):
        item = Item.objects.get(id=self.item.id)
        field_editable = item._meta.get_field('date_published').editable
        self.assertEqual(field_editable, False)

    def test_max_length_title_item(self):
        item = Item.objects.get(id=self.item.id)
        max_length = item._meta.get_field('title').max_length
        self.assertEqual(max_length, 50)

    def test_max_length_description_item(self):
        item = Item.objects.get(id=self.item.id)
        max_length = item._meta.get_field('description').max_length
        self.assertEqual(max_length, 200)

    def test_max_length_directlink_item(self):
        item = Item.objects.get(id=self.item.id)
        max_length = item._meta.get_field('directlink').max_length
        self.assertEqual(max_length, 400)

    def test_max_length_slug_item(self):
        item = Item.objects.get(id=self.item.id)
        max_length = item._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_default_value_status_item(self):
        item = Item.objects.get(id=self.item.id)
        self.assertEqual(str(item.status), '0')

    def test_name_item(self):
        item = Item.objects.get(id=self.item.id)
        name = item.title
        self.assertEqual(str(item), name)

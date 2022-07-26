from django.contrib.syndication.views import Feed as DjangoFeed
from django.template.defaultfilters import truncatewords
from .models import Item, Feed
from django.urls import reverse


class FeedItems(DjangoFeed):

    def title(self, feed):
        return feed.address

    def get_object(self, request, feed_id):
        return Feed.objects.get(pk=feed_id)

    def items(self, feed):
        return Item.objects.filter(feed=feed)

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return item.directlink

    def link(self, feed):
        return reverse("feed_items", args=[feed.id])

    def item_description(self, item):
        return truncatewords(item.description, 20)

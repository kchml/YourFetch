from django.db import models
from accounts.models import User


class Feed(models.Model):
    address = models.URLField(
        max_length=400,
        null=True)
    addressrss = models.CharField(
        max_length=400,
        null=True)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL)
    x_path = models.CharField(
        max_length=300,
        null=True)

    def __str__(self):
        return str(self.address)


class Item(models.Model):
    STATUS = (
        (0, 'zero'),
        (1, 'one'),
        (2, 'two'),
    )

    created = models.DateTimeField(
        auto_now_add=True)
    date_published = models.DateTimeField(
        null=True,
        auto_now_add=True,
        editable=False)
    title = models.CharField(
        max_length=50,
        null=True)
    description = models.CharField(
        max_length=200,
        null=True)
    feed = models.ForeignKey(
        Feed,
        null=True,
        on_delete=models.SET_NULL)
    image = models.URLField(
        null=True)
    directlink = models.URLField(
        null=True,
        max_length=400)
    slug = models.SlugField(
        max_length=200,
        unique=True,
        null=True)
    status = models.IntegerField(
        choices=STATUS,
        default=0)

    class Meta:
        ordering = ["-date_published"]

    def __str__(self):
        return self.title

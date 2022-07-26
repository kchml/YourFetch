from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import FeedForm
from .models import Item, Feed
from .scraper import get_items


@login_required
def add_site(request):
    form = FeedForm()
    if request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            site = form.save(commit=False)
            site.user = request.user
            site.save()
            messages.success(request, 'You successfully added a new feed')
            return redirect(reverse('home'))
        else:
            messages.warning(request, 'WRONG')

    context = {'form': form}
    return render(request, 'accounts/home.html', context)


@login_required
def user_page(request):
    feed_list = Feed.objects.filter(user=request.user)
    context = {'feed_list': feed_list}
    return render(request, 'feeds/userfeeds.html', context)


@login_required
def delete_site(request, feed_id):
    site = Feed.objects.get(id=feed_id, user=request.user)
    site.delete()
    return redirect(reverse('home'))


@login_required
def all_items_view(request):
    items = Item.objects.filter(feed__user=request.user)
    context = {'items': items}
    return render(request, 'feeds/items.html', context)


@login_required
def one_item_view(request, feed_id):
    items = Item.objects.filter(feed__user=request.user, feed__id=feed_id)
    context = {'items': items}
    return render(request, 'feeds/items.html', context)


@login_required
def get_feed_items(request, feed_id):
    head = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.75"}
    model_feed = Feed.objects.get(user=request.user, id=feed_id)
    scraper_data = get_items(model_feed.address, model_feed.x_path, head)
    for item_data in scraper_data:
        try:
            Item.objects.get(
                feed=model_feed,
                directlink=item_data["url"])
        except Item.DoesNotExist:
            Item.objects.create(
                feed=model_feed,
                directlink=item_data["url"],
                title=item_data["title"],
                description=item_data["description"],
                image=item_data["image_url"]
                )
    messages.success(request, "You succesed to get feed")
    return redirect(reverse('all_items_list'))


@login_required
def edit_feed(request, feed_id):
    feed = Feed.objects.get(user=request.user, id=feed_id)
    form = FeedForm(instance=feed)

    if request.method == 'POST':
        feed = FeedForm(request.POST, instance=feed)
        if feed.is_valid():
            feed.save()
            return redirect(reverse('home'))

    context = {'form': form}
    return render(request, 'feeds/editfeed.html', context)

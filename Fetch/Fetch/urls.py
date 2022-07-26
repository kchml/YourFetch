"""Fetch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import feeds.views as feeds_views
from accounts import views as accounts_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from feeds.feeds import FeedItems

urlpatterns = [
    path(
        'admin/',
        admin.site.urls),
    path(
        '',
        accounts_views.home,
        name="home"),
    path(
        'login/',
        accounts_views.login_page,
        name="login"),
    path(
        'logout/',
        accounts_views.logout_user,
        name="logout"),
    path(
        'register/',
        accounts_views.register_page,
        name="register"),
    path(
        'userfeeds/',
        feeds_views.user_page,
        name="user_feeds"),
    path(
        'addfeed/',
        feeds_views.add_site,
        name="add_feed"),
    path(
        'deletefeed/<int:feed_id>/',
        feeds_views.delete_site,
        name="delete_feed"),
    path(
        'editfeed/<int:feed_id>/',
        feeds_views.edit_feed,
        name="edit_feed"),
    path(
        'getfeeditems/<int:feed_id>/',
        feeds_views.get_feed_items,
        name="get_feed_items"),
    path(
        'feeds/<int:feed_id>/rss',
        FeedItems(),
        name="feed_items"),
    path(
        'itemslist/',
        feeds_views.all_items_view,
        name="all_items_list"),
    path(
        'itemlist/<int:feed_id>',
        feeds_views.one_item_view,
        name="one_item_list"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# YourFetch
This is a RSS feed app created with Django

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General Info
YourFetch is a rss feed app. After inputing the address of chosen site and the fragment of the html code in which there is a group of news, YourFetch will find all posts. If application encounthers a problem with finding, loading or parsing with some information, it will inform you about it in feed list.
Project  was bulit mainly with Django framework with the elements of the CSS and HTML. It was tested on Windows 10 and Ubuntu 22.04.

## Technologies
YourFetch is created with:
* Python 3.10.5
* Django 4.0.2
* Bootstrap 5
* CSS 2.1
* HTML 5

## Setup
Clone repository:

```
$ git clone https://github.com/kchml/YourFetch
```

Then using powershell go to directory with requirements.txt and install all libraries listed in it, f.e.:

```
$ pip install -r requirements.txt
```

Next go to directory with file manage.py and input in console:

```
$ python manage.py runserver
```

After that quit the server to migrate files using:

```
$ python manage.py migrate
```

Now you can input again:

```
$ python manage.py runserver
```

## Features
* Creating account
* Getting RSS address
* Parsing all information from the site which were pointed
* Listing all feeds with title, image, directlink and description

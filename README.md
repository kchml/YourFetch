# YourFetch
This is a RSS feed app created with Django

## Table of Contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [How to use YourFetch](#how-to-use-yourfetch)
* [Features](#features)

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
Doing instructions below please use terminal. Make sure that you have Pip and the newest Python installed. 
Choose where you want to download repository and clone it using:

```
$ git clone https://github.com/kchml/YourFetch
```

Then go to a directory with requirements.txt or open terminal there and install all libraries listed in it, f.e.:

```
$ pip install -r requirements.txt
```

Next go to directory with file manage.py:

```
$ cd Fetch
```

And input in console:

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

## How to use YourFetch
The first thing which you have to do is creating an account. You have to input a username, an email and a password. A password has to have at least one big letter, one number and one special sign.
When you log in, you will see searchbox with two fields. In the first field you have to input the address of the website with list of news/articles from which you want to get feeds.
The second field belongs to a xpath address. You have input a pattern of a places where would be links of addresses to whole articles. I recommend to read basic rules of a xpath syntax. If you still are not sure how it works, you can use link below to the video where I show how to add new feed address.

https://youtu.be/n-XFcIilpMA

After you add address, you should go to the "All followed sites" and click a green button. If you have done everything correctly, you would be redirected to feed list, and you would see all feed from the site.


## Features
* Creating account
* Getting RSS address
* Parsing all information from the site which were pointed
* Listing all feeds with title, image, directlink and description

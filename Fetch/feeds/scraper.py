import requests
from bs4 import BeautifulSoup
from lxml import html as lh


def get_items(url, x_path, head):
    response = requests.get(url, headers=head)

    if response.status_code != 200:

        return None

    tree = lh.fromstring(response.text)
    items_list = []
    items = tree.xpath(x_path)

    for item in items:
        item_dictionary = {}

        item_dictionary["url"] = item.get('href')
        item_dictionary["title"] = None
        item_dictionary["description"] = None
        item_dictionary["image_url"] = None

        if item_dictionary["url"].startswith("http"):
            item_dictionary_details = get_item_details(item_dictionary["url"])
            item_dictionary.update(item_dictionary_details)
            items_list.append(item_dictionary)
        else:
            items_list.append(item_dictionary)

    return items_list


def get_details_title(soup_details):
    title = soup_details.find('title')

    if title:
        return title.text
    else:
        return None


def get_details_description(soup_details):
    description = soup_details.find('meta', {"name": "description"})

    if description:
        return description['content']
    else:
        return None


def get_details_image_url(soup_details):
    image_url = soup_details.find('meta', {"property": "og:image"})

    if image_url:
        return image_url['content']
    else:
        return None


def get_item_details(url_details):
    response_details = requests.get(url_details)

    if response_details.status_code != 200:
        item_dictionary_details = {}

        item_dictionary_details["title"] = None
        item_dictionary_details["description"] = None
        item_dictionary_details["image_url"] = None

        return item_dictionary_details

    soup_details = BeautifulSoup(response_details.text, 'lxml')
    item_dictionary_details = {}

    item_dictionary_details["title"] = get_details_title(soup_details)

    item_dictionary_details["description"] = get_details_description(
        soup_details)

    item_dictionary_details["image_url"] = get_details_image_url(soup_details)

    return item_dictionary_details

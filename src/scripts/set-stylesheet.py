#!/usr/bin/env python3

from bs4 import BeautifulSoup
import logging
import os
from pprint import pformat
import requests
import sys

#logging.basicConfig(level='DEBUG')

def get_css_path(html_path):
    soup = BeautifulSoup(open(html_path), 'html.parser')
    try:
        return soup.find('link', rel='stylesheet').get('href')
    except:
        return None

def stylesheet_replace(html_path):
    with open(html_path) as f:
        soup = BeautifulSoup(f, 'html.parser')

        for stylesheet in soup.find_all('link', rel='stylesheet'):
            stylesheet.decompose()
        local_css_tag = soup.new_tag('link', rel='stylesheet', type='text/css', href='manual.css')
        soup.find_all('link')[-1].append(local_css_tag)

    with open(html_path, 'wb') as f:
        f.write(soup.prettify("utf-8"))

def stylesheet_remove(html_path):
    with open(html_path) as f:
        soup = BeautifulSoup(f, 'html.parser')

        for stylesheet in soup.find_all('link', rel='stylesheet'):
            stylesheet.decompose()

    with open(html_path, 'wb') as f:
        f.write(soup.prettify("utf-8"))

if __name__ == '__main__':
    css = sys.argv[1]
    first_html_path = sys.argv[2]

    if css == "yes":
        # Download the css file and set each html file to use it
        web_css_path = get_css_path(first_html_path)
        local_css_path = None
        if not web_css_path is None:
            local_css_path = os.path.join(os.path.dirname(first_html_path), "manual.css")
            try:
                r = requests.get(web_css_path)
                open(local_css_path, 'wb').write(r.content)
            except:
                logging.warning("Couldn't download css_path '" + web_css_path + "'")
        if not local_css_path is None:
            for html_path in sys.argv[2:]:
                stylesheet_replace(html_path)
        else:
            css == "no"

    if css == "no":
        for html_path in sys.argv[2:]:
            stylesheet_remove(html_path)

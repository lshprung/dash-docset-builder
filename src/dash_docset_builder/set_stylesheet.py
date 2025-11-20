#!/usr/bin/env python3

from bs4 import BeautifulSoup
import logging
import os
import requests
import sys

class Stylesheet_Setter:
    def __init__(self, css: bool, first_html_path: str) -> None:
        if css == True:
            # Download the css file and set each html file to use it
            web_css_path = self.get_css_path(first_html_path)
            local_css_path = None
            if not web_css_path is None:
                local_css_path = os.path.join(
                        os.path.dirname(first_html_path), 
                        "manual.css"
                )
                try:
                    r = requests.get(str(web_css_path))
                    _ = open(local_css_path, 'wb').write(r.content)
                except:
                    logging.warning(
                            f"Couldn't download css_path '{str(web_css_path)}'"
                    )
            if not local_css_path is None:
                for html_path in sys.argv[2:]:
                    self.stylesheet_replace(html_path)
            else:
                css = False

        if css == False:
            for html_path in sys.argv[2:]:
                self.stylesheet_remove(html_path)

    def get_css_path(self, html_path: str):
        soup = BeautifulSoup(open(html_path), 'html.parser')
        try:
            return soup.find('link', rel='stylesheet').get('href')
        except:
            return None

    def stylesheet_replace(self, html_path: str) -> None:
        with open(html_path) as f:
            soup = BeautifulSoup(f, 'html.parser')

            for stylesheet in soup.find_all('link', rel='stylesheet'):
                stylesheet.decompose()
            local_css_tag = soup.new_tag(
                    'link', 
                    rel='stylesheet', 
                    type='text/css', 
                    href='manual.css'
            )
            _ = soup.find_all('link')[-1].append(local_css_tag)

        with open(html_path, 'wb') as f:
            _ = f.write(soup.prettify("utf-8"))

    def stylesheet_remove(self, html_path: str) -> None:
        with open(html_path) as f:
            soup = BeautifulSoup(f, 'html.parser')

            for stylesheet in soup.find_all('link', rel='stylesheet'):
                stylesheet.decompose()

        with open(html_path, 'wb') as f:
            _ = f.write(soup.prettify("utf-8"))


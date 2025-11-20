#!/usr/bin/env python3

from bs4 import BeautifulSoup
import sys

def get_title(html_path): 
    soup = BeautifulSoup(open(html_path), 'html.parser')
    title = soup.title.get_text()
    # Remove newline characters
    title = title.replace('\n', '')
    # Replace '"' with '""' for sake of support in sqlite insertion
    title = title.replace('"', '""')

    return title

if __name__ == '__main__':
    print(get_title(sys.argv[1]))

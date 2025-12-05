from bs4 import BeautifulSoup
from pathlib import Path

def get_title(html_path: Path) -> str: 
    """! Get the title tag text from an html file
    
    @param html_path    path to html file to get title from

    Additionally, some sanitization is performed on the title: removal of 
    newline characters and replacement of double quotes with two double 
    quotes for sqlite insertion
    """

    soup = BeautifulSoup(open(html_path), 'html.parser')
    if soup.title is None:
        return ''
    title = soup.title.get_text()
    # Remove newline characters
    title = title.replace('\n', '')
    # Replace '"' with '""' for sake of support in sqlite insertion
    title = title.replace('"', '""')

    return title

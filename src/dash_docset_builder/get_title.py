from bs4 import BeautifulSoup

def get_title(html_path: str) -> str: 
    soup = BeautifulSoup(open(html_path), 'html.parser')
    if soup.title is None:
        return ''
    title = soup.title.get_text()
    # Remove newline characters
    title = title.replace('\n', '')
    # Replace '"' with '""' for sake of support in sqlite insertion
    title = title.replace('"', '""')

    return title

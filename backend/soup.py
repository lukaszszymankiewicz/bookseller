import bs4


def create_soup(page_content: str) -> bs4.BeautifulSoup:
    return bs4.BeautifulSoup(page_content, "html.parser")

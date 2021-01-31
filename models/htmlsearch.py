import re
from typing import Callable

import bs4


class HTMLSearch:
    def __init__(
        self,
        tag: str,
        attrs: dict,
        cleaning_regex: str,
        cleaning_replace: dict = ("", ""),
        convertion_fun=float,
        aggregate_fun: Callable = lambda x: x,
    ):
        self.tag = tag
        self.attrs = attrs
        self.cleaning_regex = cleaning_regex
        self.cleaning_replace = cleaning_replace
        self.convertion_fun = convertion_fun
        self.aggregate_fun = aggregate_fun

    def clean_tag(self, tag: str):
        tag_regexed = re.search(self.cleaning_regex, tag.text)[0]
        tag_cleaned = tag_regexed.replace(*self.cleaning_replace)
        tag_cleaned_and_converted = self.convertion_fun(tag_cleaned)

        return tag_cleaned_and_converted

    def search(self, soup: bs4.BeautifulSoup):
        tags = soup.findAll(name=self.tag, attrs=self.attrs)
        cleaned_searches = [self.clean_tag(tag) for tag in tags]
        aggregated_results = self.aggregate_fun(cleaned_searches)

        return aggregated_results


prices_search = HTMLSearch(
    tag="span",
    attrs={"class": "_1svub _lf05o"},
    cleaning_regex="[+-]?([0-9]*[,])?[0-9]+",
    cleaning_replace=(",", "."),
    convertion_fun=float,
    aggregate_fun=lambda x: sum(x) // len(x),
)
sales_number_search = HTMLSearch(
    tag="span",
    attrs={"class": "msa3_z4"},
    cleaning_regex="[0-9]*",
    convertion_fun=int,
    aggregate_fun=lambda x: sum(x),
)

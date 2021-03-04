import re
from functools import partial
from typing import Callable, Tuple

import bs4

from .math import save_division


def parse_soup(
    tag: str,
    attrs: dict,
    cleaning_regex: str,
    cleaning_replace: Tuple[str],
    convertion_fun: Callable,
    aggregate_fun: Callable,
    soup: bs4.BeautifulSoup,
):
    cleaned_tags = []

    tags = soup.findAll(name=tag, attrs=attrs)

    import pdb

    pdb.set_trace()
    for tag in tags:
        tag_regexed = re.search(cleaning_regex, tag.text)[0]
        tag_cleaned = tag_regexed.replace(*cleaning_replace)
        tag_cleaned_and_converted = convertion_fun(tag_cleaned)

        cleaned_tags.append(tag_cleaned_and_converted)

    aggregated_results = aggregate_fun(cleaned_tags)

    return aggregated_results


prices_search = partial(
    parse_soup,
    tag="span",
    attrs={"class": "_1svub _lf05o"},
    cleaning_regex="[+-]?([0-9]*[,])?[0-9]+",
    cleaning_replace=(",", "."),
    convertion_fun=float,
    aggregate_fun=save_division,
)

sales_number_search = partial(
    parse_soup,
    tag="span",
    attrs={"class": "msa3_z4"},
    cleaning_regex="[0-9]*",
    convertion_fun=int,
    cleaning_replace=("", ""),
    aggregate_fun=lambda x: sum(x),
)

number_of_result_pages = partial(
    parse_soup,
    tag="span",
    attrs={"class": "_1h7wt _1fkm6 _g1gnj _3db39_3i0GV _3db39_XEsAE"},
    cleaning_regex="[0-9]*",
    convertion_fun=int,
    cleaning_replace=("", ""),
    aggregate_fun=lambda x: x[0],
)

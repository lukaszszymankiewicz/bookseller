import re
from functools import partial
from typing import Callable, Tuple

import bs4

from .aggregation_functions import (avg_from_list, force_sum, force_to_float,
                                    force_to_int)


def parse_soup_single_entities(
    tag: str,
    attrs: dict,
    soup: bs4.BeautifulSoup,
):
    return soup.find(name=tag, attrs=attrs).text


def parse_soup_many_entities(
    tag: str,
    attrs: dict,
    cleaning_regex: str,
    cleaning_replace: Tuple[str],
    convertion_fun: Callable,
    aggregate_fun: Callable,
    soup: bs4.BeautifulSoup,
):
    """
    Parses BeautifulSoup (using 'tag' and 'args' parameters), clean and aggregate results.
    """
    cleaned_tags = []

    tags = soup.findAll(name=tag, attrs=attrs)

    for tag in tags:
        if cleaning_regex:
            tag_regexed = re.search(cleaning_regex, tag.text)[0]
        tag_cleaned = tag_regexed.replace(*cleaning_replace)
        tag_cleaned_and_converted = convertion_fun(tag_cleaned)

        cleaned_tags.append(tag_cleaned_and_converted)

    aggregated_results = aggregate_fun(cleaned_tags)

    return aggregated_results


prices_search = partial(
    parse_soup_many_entities,
    tag="span",
    attrs={"class": "_1svub _lf05o"},
    cleaning_regex="[+-]?([0-9]*[,])?[0-9]+",
    cleaning_replace=(",", "."),
    convertion_fun=force_to_float,
    aggregate_fun=avg_from_list,
)

sales_number_search = partial(
    parse_soup_many_entities,
    tag="span",
    attrs={"class": "msa3_z4"},
    cleaning_regex="[0-9]*",
    convertion_fun=force_to_int,
    cleaning_replace=("", ""),
    aggregate_fun=force_sum,
)

number_of_result_pages = partial(
    parse_soup_many_entities,
    tag="span",
    attrs={"class": "_1h7wt _1fkm6 _g1gnj _3db39_3i0GV _3db39_XEsAE"},
    cleaning_regex="[0-9]*",
    convertion_fun=force_to_int,
    cleaning_replace=("", ""),
    aggregate_fun=lambda x: x[0],
)

title_search = partial(
    parse_soup_single_entities,
    tag="span",
    attrs={"id": "describe-isbn-title", "itemprop": "name"},
)

author_search = partial(
    parse_soup_single_entities,
    tag="span",
    attrs={"itemprop": "author"},
)

sales_number_search = partial(
    parse_soup_many_entities,
    tag="span",
    attrs={"class": "msa3_z4"},
    cleaning_regex="[0-9]*",
    convertion_fun=force_to_int,
    cleaning_replace=("", ""),
    aggregate_fun=force_sum,
)

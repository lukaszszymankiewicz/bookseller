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
    """
    Parses BeautifulSoup for search in particual HTML tag. Only the first occurance is recorded.

    Args:
        tag - HTML tag to be found in Soup (function will found ALL occurances of this tag).
        attrs - dict containing specific HTML attributes which tag mus have to be considered proper,
        soup - BeautiflSoup instance.
    """
    result = soup.find(name=tag, attrs=attrs)

    if not result:
        return None

    return result.text


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
    Parses BeautifulSoup for specific thing to be found in it. Additional cleanup and aggregation
    are also performed.

    Args:
        tag - HTML tag to be found in Soup (function will found ALL occurances of this tag).
        attrs - dict containing specific HTML attributes which tag mus have to be considered proper,
        cleaning_regex - regex filte to be performed on every tag content,
        cleaning_replace - arguments for Python 'replace' function (for additional string cleaning),
        convertion_fun - function to be used to convert found values (rg.: float to integers),
        aggregate_fun - function to be used on all founded results (after all cleanups) to generate
            single result (eg.: sum of all elements),
        soup - BeautiflSoup instance.

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

sales_number_search = partial(
    parse_soup_many_entities,
    tag="span",
    attrs={"class": "msa3_z4"},
    cleaning_regex="[0-9]*",
    convertion_fun=force_to_int,
    cleaning_replace=("", ""),
    aggregate_fun=force_sum,
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

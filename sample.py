import pickle
import re
from functools import partial

import bs4
import requests


def avg_from_list(x):
    if len(x) == 0:
        return 0
    else:
        return sum(x) // len(x)


def parse_soup(
    tag: str,
    attrs: dict,
    cleaning_regex: str,
    cleaning_replace,
    convertion_fun,
    aggregate_fun,
    soup,
):
    cleaned_tags = []

    tags = soup.findAll(name=tag, attrs=attrs)

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
    aggregate_fun=avg_from_list,
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
# /* sigh */
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
}
urls = [
    "https://allegro.pl/kategoria/ksiazki-i-komiksy?string=Krzyżacy Henryk Sienkiewicz&order=qd",
    "https://allegro.pl/kategoria/ksiazki-i-komiksy?string=Pan Tadeusz Adam Mickiewicz&order=qd",
    "https://allegro.pl/kategoria/ksiazki-i-komiksy?string=Jebanie Policji Rychu Peja&order=qd",
]
for number, url in enumerate(urls):
    request = requests.get(url=url, headers=headers)

    print(f"request sent for url {number}")
    soup = bs4.BeautifulSoup(request.content, "html.parser")

    # checking
    prices = prices_search(soup=soup)
    print(prices)

    file = open(f"pickle_{number}.pkl", "wb")
    pickle.dump(str(soup), file)
    file.close()

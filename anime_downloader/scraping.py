import re
from typing import List

import requests
from bs4 import BeautifulSoup, Tag

from anime_downloader import consts


BASE_URL = 'https://nyaa.si'
SEARCH_URL_FORMAT = BASE_URL + '/?q={source}+{anime}+{resolution}/'


def _get_magnet(url: str) -> str:
    soup = BeautifulSoup(requests.get(url).content, features='html.parser')
    return str(soup.find('a', {'class': 'card-footer-item'})['href'])


def _get_episode_tags(soup: BeautifulSoup) -> List[Tag]:
    ret = []
    success_tags = soup.find_all('tr')
    for tag in success_tags:
        a_tags = tag.find_all('a')
        ret += [a for a in a_tags if re.match(consts.ANIME_PATTERN, str(a.string))]
    return ret


def _get_relevant_tags(episode_tags: List[Tag], last_episode: int) -> List[Tag]:
    ret = []
    for tag in episode_tags:
        _, number = re.match(consts.ANIME_PATTERN, tag.string).groups()
        number = int(number)
        if number > last_episode:
            ret.append(tag)
    return ret


def get_magnets(source: str, anime: str, resolution: str, last_episode: int) -> List[str]:
    url = SEARCH_URL_FORMAT.format(source=source, anime=anime, resolution=resolution)
    soup = BeautifulSoup(requests.get(url).content, features='html.parser')
    episode_tags = _get_episode_tags(soup)
    relevant_tags = _get_relevant_tags(episode_tags, last_episode)
    return [_get_magnet(BASE_URL + tag['href']) for tag in relevant_tags]

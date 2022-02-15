import re
from typing import List

import requests
from bs4 import BeautifulSoup, Tag

from anime_downloader import consts
from anime_downloader.types import TorrentMetadata


BASE_URL = 'https://nyaa.si'
SEARCH_URL_FORMAT = BASE_URL + '/?q={source}+{anime}+{resolution}/'


def _get_torrent_metadata(url: str) -> TorrentMetadata:
    soup = BeautifulSoup(requests.get(url).content, features='html.parser')
    name = soup.find('h3', {'class': 'panel-title'}).text.strip()
    links = soup.find('div', {'class': 'panel-footer'}).find_all('a')
    url = BASE_URL + links[0]['href']
    magnet = links[1]['href']
    return TorrentMetadata(name, url, magnet)


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
    return [_get_torrent_metadata(BASE_URL + tag['href']).magnet for tag in relevant_tags]

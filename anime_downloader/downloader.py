import re
import logging
from threading import Thread
from typing import Dict, List, Tuple

from anime_downloader import consts, scraping
from anime_downloader.torrent_manager import TorrentManager


class Downloader:
    def __init__(self, anime, download_path):
        self.anime = anime
        self.anime_names = [a['name'] for a in anime]
        self.download_path = download_path

        self.logger = logging.getLogger(type(self).__name__)
        self.torrent = None
        self.downloaded = 0

    def _find_anime_torrent_data(self, torrent) -> Tuple[str, int]:
        match = re.match(consts.ANIME_PATTERN, torrent.name)
        if not match:
            raise ValueError(f'Torrent is not an anime: "{torrent.name}"')
        
        anime, episode = match.groups()
        if anime not in self.anime_names:
            raise ValueError(f'Untracked anime: {anime}')

        return anime, int(episode)
    
    def find_latest_episodes(self) -> Dict[str, int]:
        latest_episodes = dict()
        torrents = self.torrent.get_torrents()
        for t in torrents:
            try:
                anime, episode = self._find_anime_torrent_data(t)
            except ValueError:
                continue
            latest_episode = latest_episodes.get(anime, 0)
            if episode > latest_episode:
                latest_episodes[anime] = episode
        return latest_episodes
    
    def download_magnets(self, magnets: List[str]):
        for magnet in magnets:
            self.torrent.download_magnet(magnet, self.download_path)
            self.downloaded += 1
    
    def handle_anime(self, name: str, resolution: str, source: str, latest_episode: int):
        self.logger.info(f'{name}\'s latest local episode is {latest_episode}')
        magnets = scraping.get_magnets(source, name, resolution, latest_episode)
        self.logger.info(f'Found {len(magnets)} magnets for {name}')
        self.download_magnets(magnets)
    
    def _download_anime(self):
        latest_episodes = self.find_latest_episodes()
        threads = list()
        for anime in self.anime:
            latest_episode = latest_episodes[anime['name']]
            thread = Thread(target=self.handle_anime, kwargs=dict(latest_episode=latest_episode, **anime))
            thread.start()
            threads.append(thread)
        [thread.join() for thread in threads]

    def download_anime(self):
        try:
            self.torrent = TorrentManager()
            self._download_anime()
        except Exception as e:
            self.logger.exception(f'Exception raised: {e}')
        finally:
            self.logger.info(f'Added {self.downloaded} magnets')

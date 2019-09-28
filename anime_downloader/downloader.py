import re
import logging
import traceback
from typing import Dict, List, Tuple

from anime_downloader import config, consts, horriblesubs
from anime_downloader.torrent_manager import TorrentManager, Torrent


def _find_anime_torrent_data(torrent: Torrent) -> Tuple[str, int]:
    match = re.match(consts.ANIME_PATTERN, torrent.name)
    if not match:
        raise ValueError(f'Torrent is not an anime: "{torrent.name}"')
    
    anime, episode = match.groups()
    if anime not in config.anime:
        raise ValueError(f'Untracked anime: {anime}')

    return anime, int(episode)

class Downloader:
    def __init__(self):
        self.torrent = None
        self.downloaded = 0
    
    def find_latest_episodes(self) -> Dict[str, int]:
        latest_episodes = {anime: 0 for anime in config.anime}
        torrents = self.torrent.get_torrents()
        for t in torrents:
            try:
                anime, episode = _find_anime_torrent_data(t)
            except ValueError:
                continue
            latest_episode = latest_episodes[anime]
            if episode > latest_episode:
                latest_episodes[anime] = episode
        return latest_episodes
    
    def download_magnets(self, magnets: List[str]):
        for magnet in magnets:
            self.torrent.download_magnet(magnet, config.download_path)
            self.downloaded += 1
    
    def handle_anime(self, anime: str, latest_episode: int):
        logging.info(f'{anime}\'s latest local episode is {latest_episode}')
        magnets = horriblesubs.get_magnets(anime, config.resolution, latest_episode)
        logging.info(f'Found {len(magnets)} magnets for {anime}')
        self.download_magnets(magnets)

    def download_anime(self):
        try:
            self.torrent = TorrentManager()
            latest_episodes = self.find_latest_episodes()
            for anime, latest_episode in latest_episodes.items():
                self.handle_anime(anime, latest_episode)
        except Exception as e:
            logging.error(f'Exception raised: {e}')
            traceback.print_tb(e.__traceback__)
        finally:
            logging.info(f'Downloaded {self.downloaded} files')
            input('Finished!')
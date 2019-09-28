from typing import List

from qbittorrent import Client

from .types import Torrent

class TorrentManager:
    def __init__(self, host: str = 'http://localhost:8080'):
        self.client = Client(host)
    
    def get_torrents(self) -> List[Torrent]:
        torrents_data = self.client.torrents()
        return [Torrent(**torrent_data) for torrent_data in torrents_data]
    
    def download_magnet(self, magnet: str, directory: str):
        self.client.download_from_link(magnet, savepath=directory)

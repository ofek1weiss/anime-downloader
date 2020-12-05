from typing import List

import qbittorrentapi
import qbittorrent

class TorrentManager:
    def __init__(self):
        self.client = qbittorrentapi.Client('localhost:8080')
    
    def get_torrents(self) -> List:
        return self.client.torrents_info()
    
    def download_magnet(self, magnet: str, directory: str):
        self.client.torrents_add(magnet, save_path=directory)

from dataclasses import dataclass


@dataclass
class TorrentMetadata:
    name: str
    url: str
    magnet: str

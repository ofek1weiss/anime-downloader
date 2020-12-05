import json
import logging
from pathlib import Path

from anime_downloader.downloader import Downloader

logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)

CONFIG_PATH = Path(__file__).parent / 'config.json'


def main():
    with CONFIG_PATH.open() as f:
        config = json.load(f)
    Downloader(**config).download_anime()
    input('Finished!')


if __name__ == "__main__":
    main()

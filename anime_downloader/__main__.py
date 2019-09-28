import logging

from anime_downloader.downloader import Downloader

logging.basicConfig(format='[%(asctime)s] %(levelname)s - %(message)s', level=logging.INFO)


def main():
    Downloader().download_anime()


if __name__ == "__main__":
    main()

from setuptools import find_packages, setup

setup(
    name='anime_downloader',
    version='1.0.0',
    include_package_data=True,
    requires=[
        'python_qbittorrent',
        'attrs',
        'beautifulsoup4',
        'requests'
    ],
    entry_points = {
        'console_scripts': [
            'download-anime=anime_downloader.__main__:main'
        ],
    }
)
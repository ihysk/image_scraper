from setuptools import find_packages
from setuptools import setup


setup(
    name='image_scraper',
    version='0.0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'imsc=scraper.scraper:scraping',
        ],
    },
)

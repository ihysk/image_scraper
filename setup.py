from setuptools import setup


setup(
    name='image_scraper',
    version='0.0.1',
    packages=['scraper'],
    entry_points={
        'console_scripts': [
            'imsc=scraper.scraper:scraping',
        ],
    },
)

from setuptools import find_packages
from setuptools import setup


setup(
    name='image_scraper',
    version='0.0.2',
    description='Image collector by selenium',
    long_description='A tool to collect images which matches specific keyword',
    url='https://github.com/ihysk/image_scraper',
    author='ihysk',
    author_email='sirouma.09@gmail.com',
    license='MIT',
    install_requires=['opencv-python', 'requests', 'selenium'],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'imsc=scraper.scraper:scraping',
        ],
    },
)

import os
import re
import requests
import sys
from selenium import webdriver
from lib.pom.Home import Home
from lib.util.Logger import get_module_logger

images_dir = 'images'


def save_image(url, name):
    response = requests.get(url)

    filename = re.split('/', url)
    path, ext = os.path.splitext(filename[-1])
    path = os.path.join(images_dir, name + ext)

    with open(path, "wb") as fout:
        fout.write(response.content)


def scraping():
    driver = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')
    driver.get('https://www.google.co.jp/imghp?hl=ja')
    logger = get_module_logger(__name__)

    home = Home(driver)
    keyword = sys.argv[1]
    search = home.search_with_string(keyword)
    search.scroll_down_to_display_all_images()
    urls = search.get_image_urls()

    for i, url in enumerate(urls):
        save_image(url, keyword + '_' + str(i))

    driver.quit()


if __name__ == '__main__':
    scraping()

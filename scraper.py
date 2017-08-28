import os
import re
import requests
from selenium import webdriver
from lib.pom.Home import Home
from lib.util.Logger import get_module_logger

search_str = 'test'
images_dir = 'images'


def save_image(url):
    response = requests.get(url)

    filename = re.split('/', url)
    path = os.path.join(images_dir, filename[-1])

    with open(path, "wb") as fout:
        fout.write(response.content)


driver = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')
driver.get('https://www.google.co.jp/imghp?hl=ja')
logger = get_module_logger(__name__)

home = Home(driver)
search = home.search_with_string(search_str)
urls = search.get_image_urls()

for url in urls:
    save_image(url)

driver.quit()

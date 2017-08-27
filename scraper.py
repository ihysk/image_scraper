import os
import re
import requests
from selenium import webdriver
from lib.pom.Home import Home
from lib.util.Logger import get_module_logger

search_str = 'test'
images_dir = 'images'

driver = webdriver.Chrome(executable_path='/Users/ikuma/Downloads/chromedriver')
driver.get('https://www.google.co.jp/imghp?hl=ja')
logger = get_module_logger(__name__)

home = Home(driver)
search = home.search_with_string(search_str)
urls = search.get_image_urls()

for url in urls:
    response = requests.get(url)

    # get file name from the path
    paths = re.split('/', url)
    full_path = os.path.join('images', paths[-1])

    with open(full_path, "wb") as fout:
        fout.write(response.content)

driver.quit()

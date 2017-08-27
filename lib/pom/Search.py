import re
import urllib.parse
from lib.util.Logger import get_module_logger


class Search:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_module_logger(__name__)

    def get_search_results(self):
        return self.driver.find_element_by_id('search')

    def get_image_urls(self):
        urls = []
        elems = self.get_search_results().find_elements_by_class_name('rg_l')
        for elem in elems:
            # Split href string with ? and &
            parames = re.split('[?&]', elem.get_attribute('href'))
            # URI decoded query parameter assigned to imgurl=
            url = urllib.parse.unquote(parames[1].lstrip('imgurl='))
            # Only param which has 'http(s)' will be stored in list
            if url.find('http') != -1:
                self.logger.debug(url)
                urls.append(url)

        return urls

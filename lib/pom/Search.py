from lib.util.Logger import get_module_logger


class Search:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_module_logger(__name__)

    def get_search_results(self):
        return self.driver.find_element_by_id('search')

    def get_image_urls(self):
        elems = self.get_search_results().find_elements_by_class_name('rg_l')
        for elem in elems:
            self.logger.debug(elem.get_attribute('href'))

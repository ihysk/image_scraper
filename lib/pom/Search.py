from lib.util.Logger import get_module_logger


class Search:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_module_logger(__name__)

    def get_search_bar(self):
        return self.driver.find_element_by_id('search')

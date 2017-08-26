from lib.util.Logger import get_module_logger
from lib.pom.Search import Search


class Home:

    def __init__(self, driver):
        self.driver = driver
        self.logger = get_module_logger(__name__)

    def get_search_bar(self):
        return self.driver.find_element_by_id('sfdiv')

    def get_search_field(self):
        return self.get_search_bar().find_element_by_id('lst-ib')

    def get_search_button(self):
        return self.get_search_bar().find_element_by_name('btnG')

    def search_with_string(self, str):
        input = self.get_search_field()
        input.send_keys(str)
        self.get_search_button().click()
        self.logger.debug('Googling {} images...'.format(str))
        return Search(self.driver)

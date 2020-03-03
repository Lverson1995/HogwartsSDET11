from appium.webdriver.common.mobileby import MobileBy

from homework20200301.page.base_page import BasePage
# from homework20200301.page.search import Search


class Stocks(BasePage):
    def goto_search_page(self):
        from homework20200301.page.search import Search
        self.find(MobileBy.ID,'action_search').click()
        return Search(self._driver)
    def get_msg(self):
        return self.find_and_get_text(MobileBy.XPATH,"//*[@text='自选股' and contains(@resource-id,'title')]")

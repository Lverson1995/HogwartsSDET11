from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from homework20200301.page.base_page import BasePage
from homework20200301.page.profile import Profile
from homework20200301.page.search import Search

# from homework20200301.page.stocks_page import Stocks


class Main(BasePage):
    # 进入搜索页
    def goto_search_page(self):
        self.find(MobileBy.ID, "tv_search").click()
        return Search(self._driver)

    # 进入行情页
    def goto_stocks(self):
        from homework20200301.page.stocks_page import Stocks
        self.find(MobileBy.XPATH, "//*[@text='行情' and contains(@resource-id,'tab')]").click()
        return Stocks(self._driver)

    def goto_trade(self):
        pass

    def goto_profile(self):
        self.find(By.XPATH, "//*[@text='我的']").click()
        return Profile(self._driver)

    def goto_messages(self):
        pass

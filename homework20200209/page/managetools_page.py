from selenium.webdriver.common.by import By

from homework20200209.page.base_page import BasePage
from homework20200209.page.material_library_page import MaterialLibrary


class ManageToolsPage(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#manageTools"
    #素材库入口
    def goto_material_library(self):
        #进入素材库
        self._driver.find_elements(By.CSS_SELECTOR,".manageTools_cnt_item")[5].click()
        return MaterialLibrary(reuse=True)
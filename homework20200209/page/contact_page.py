from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from homework20200209.page.base_page import BasePage


class Contact(BasePage):
    _add_member_button=(By.CSS_SELECTOR,"xxx")
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    def add_member(self, data):
        #self.driver.find_element("添加成员").click
        #sendkeys
        #click save
        name_locator = (By.NAME, 'username')
        acctid_locator = (By.NAME, 'acctid')
        # $('.ww_radio[value="2"]')
        gender_locator = (By.CSS_SELECTOR, '.ww_radio[value="2"]')
        mobile_locator = (By.NAME, 'mobile')
        self.find(name_locator).send_keys("yangyangyang")
        self.find(acctid_locator).send_keys("yangyangyang")
        self.find(gender_locator).click()
        self.find((By.CSS_SELECTOR, ".ww_telInput_zipCode_input")).click()
        #self.find((By.CSS_SELECTOR, 'li[data-value="853"]')).click()
        self.find(mobile_locator).send_keys("13456324576")
        self.find(By.LINK_TEXT,"保存").click()
        return self

    def goto_add_member(self):
        WebDriverWait(self._driver, 20).until(self.wait_element)
        return self

    #todo 鼠标悬浮后显示成员列表后边的3点，点击也可以编辑
    def edit_member(self,selectData,editData):
        self.find(By.CSS_SELECTOR,'td[title="%s"]'% selectData).click()
        self.find(By.LINK_TEXT,"编辑").click()

        name_locator = (By.NAME, 'username')
        self.find(name_locator).clear()
        self.find(name_locator).send_keys(editData)
        self.find(By.LINK_TEXT, "保存").click()
        return self

    def wait_element(self, x):
        size = len(self._driver.find_elements(By.ID, 'username'))
        if size < 1:
            self._driver.find_element(By.CSS_SELECTOR, '.js_has_member div:nth-child(1) .js_add_member').click()
        return size >= 1






from time import sleep

from selenium.webdriver.common.by import By

from homework20200209.page.base_page import BasePage


class MaterialLibrary(BasePage):
    _base_url="https://work.weixin.qq.com/wework_admin/frame#material/text"
    def add_text(self):
        pass

    def add_graphic(self):
        pass

    def add_image(self,path,app):
        self.find(By.LINK_TEXT,"图片").click()
        self.find(By.LINK_TEXT,"添加图片").click()
        self.find(By.ID,"js_upload_input").send_keys(path)
        self.find(By.LINK_TEXT,"选择").click()
        self.find(By.CSS_SELECTOR,'label[data-name="%s"]'% app).click()
        self.find(By.LINK_TEXT,"确定").click()
        self.find(By.LINK_TEXT, "完成").click()
        return self

    def add_voice(self):
        pass

    def add_video(self):
        pass

    def add_file(self):
        pass

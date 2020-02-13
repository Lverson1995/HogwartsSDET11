from time import sleep

from selenium.webdriver.common.by import By

from homework20200209.page.base_page import BasePage
from homework20200209.page.contact_page import Contact
from homework20200209.page.message import Message


class Main(BasePage):
    _base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    #对于需要返回断言内容的部分，直接返回内容即可

    def download(self):
        pass

    # 在当前页面操作，操作完返回self
    def import_user(self, path):
        self.find((By.PARTIAL_LINK_TEXT, "导入成员")).click()
        self.find((By.LINK_TEXT, "批量导入")).click()
        # input类型标签上传，使用send_keys
        self.find(By.ID, "js_upload_file_input").send_keys(path)
        #todo 显式等待
        sleep(5)
        self.find((By.ID, "submit_csv")).click()
        self.find((By.ID, "reloadContact")).click()
        return self

    def goto_app(self):
        pass

    def goto_company(self):
        pass

    # 对于需要返回断言内容的部分，直接返回内容即可
    def get_message(self):
        return ["aaa", "bbb"]

    def add_member(self):
        # todo:xxx
        # 页面按钮只是实现了一个入口，点击后进行页面的跳转，真正的功能实现在跳转的页面里
        # 跳转关系在代码里面以函数返回值的形式实现
        # 调用对应功能时进行链式调用就行
        locator = (By.LINK_TEXT, '添加成员')
        self.find(locator).click()
        # 使用js脚本实现点击示例
        # self._driver.execute_script("arguments[0].click();", self.find(locator))
        return Contact(reuse=True)

    def send_message(self):
        locator = (By.LINK_TEXT, '消息群发')
        self.find(locator).click()
        return Message(reuse=True)

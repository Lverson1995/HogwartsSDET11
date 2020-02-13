from homework20200209.page.main_page import Main


class TestMain:
    def setup(self):
        self.main = Main(reuse=True)
    def test_add_member(self):
        self.main.add_member().add_member("xxx")
        #assert "success" in self.main.get_message()

    def test_import_user(self):
        self.main.import_user(
            r"E:\horworProject\HogwartsSDET11\homework20200209\test_case\通讯录批量导入模板.xlsx")
        # assert "success" in self.main.get_message()

    def test_send_message(self):
        message = self.main.send_message();
        message.send(app="yang", content="content", group="杨")
        #assert "content" in message.get_history()
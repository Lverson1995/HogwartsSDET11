from homework20200301.page.app import App
# TODO python包循环导入问题

class TestStocks:
    def setup(self):
        self.main = App().start().main()
    def test_stocks(self):
        assert "自选股" in self.main.goto_stocks().goto_search_page().search('alibaba').add_select().cancel().get_msg()

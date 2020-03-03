from homework20200301.page.app import App
from homework20200301.page.base_page import BasePage


class TestDD:
    def test_dd(self):
        base = BasePage()
        base.steps("../page/steps.yaml")

    def test_search(self):
        App().start().main().goto_search_page().search("jd")
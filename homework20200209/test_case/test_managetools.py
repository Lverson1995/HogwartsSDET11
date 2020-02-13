from homework20200209.page.managetools_page import ManageToolsPage


class TestManageTools:
    def setup(self):
        self.manageTools=ManageToolsPage(reuse=True)

    def test_goto_material_library(self):
        self.manageTools.goto_material_library()
        #todo assert断言部分

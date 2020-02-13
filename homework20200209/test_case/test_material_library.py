from homework20200209.page.material_library_page import MaterialLibrary


class TestMaterialLibrary:
    def setup(self):
        self.materialLibrary=MaterialLibrary(reuse=True)
    def test_add_text(self):
        pass

    def test_add_graphic(self):
        pass

    #作业1  管理工具 -> 素材库 -> 图片 -> 上传
    def test_add_image(self):
        self.materialLibrary.add_image(r"E:\horworProject\HogwartsSDET11\homework20200209\test_case\logo.png","yang")
        #todo 断言上传成功

    def test_add_voice(self):
        pass

    def test_add_video(self):
        pass

    def test_add_file(self):
        pass
from homework20200412.api.department_manage import DepartmentManage


class TestDepartmentManage:
    @classmethod
    def setup_class(cls):
        cls.depart_manage = DepartmentManage()

    def test_department_manane_list(self):
        # 部门id
        department_id = 7
        r = self.depart_manage.list(department_id)
        assert r['errcode'] == 0

    def test_department_manane_create(self):
        name = "departname"
        parent_depart_id = 2
        # 可选参数，指定部门id
        id = 100
        r = self.depart_manage.create(name, parent_depart_id, id=id)
        assert r['errcode'] == 0

    def test_department_manane_update(self):
        id = 11
        name = "depart"
        r = self.depart_manage.update(id, name=name)
        assert r['errcode'] == 0

    def test_department_manane_delete(self):
        id = 11
        r = self.depart_manage.delete(id)
        assert r['errcode'] == 0

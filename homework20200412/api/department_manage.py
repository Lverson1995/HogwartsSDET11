import requests

from homework20200412.api.wework import WeWork


class DepartmentManage(WeWork):
    contact_secret = "v1lnmBnP10_KMnYE4pp2okM2ficvsB21hjZUgAKIjto"

    # 根据部门id，获取部门列表
    def list(self, department_id):
        list_url = "https://qyapi.weixin.qq.com/cgi-bin/department/list"
        r = requests.get(
            list_url,
            params={'access_token': self.get_token(self.contact_secret), 'id': department_id}
        )
        self.format(r)
        return r.json()

    # 创建部门
    def create(self, name, parentid, **kwargs):
        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        data = {
            'name': name,
            'parentid': parentid
        }
        # 非必选参数
        data.update(kwargs)
        r = requests.post(
            create_url,
            params={"access_token": self.get_token(self.contact_secret)},
            json=data
        )
        self.format(r)
        return r.json()

    # 更新部门
    def update(self, id, **kwargs):
        create_url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        data = {'id': id}
        # 非必选参数
        data.update(kwargs)
        r = requests.post(
            create_url,
            params={"access_token": self.get_token(self.contact_secret)},
            json=data
        )
        self.format(r)
        return r.json()

    def delete(self, id):
        delete_url = "https://qyapi.weixin.qq.com/cgi-bin/department/delete"
        r = requests.get(
            delete_url,
            params={"access_token": self.get_token(self.contact_secret), 'id': id},
        )
        self.format(r)
        return r.json()

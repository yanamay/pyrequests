import requests
import os,sys
import unittest
from parameterized import parameterized
from db_fixture import test_data
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

class AddGuestTest(unittest.TestCase):
    '''添加嘉宾'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/add_guest/"
    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ('all_null', '', '', '', '', 10021, '参数不能为空'),
        ('eid_type_err', 'ssss', 'tang', 15181001182, '836096399@qq.com',10022, 'eid格式错误'),
        ('phone_type_err', 2, 'tang', False, '836096399@qq.com', 10023, 'phone格式错误'),
        ('eid_not_exist', 7, 'tang', 15181001182, '836096399@qq.com', 10024, 'Event id为空'),
        ('event_not_start', 4, 'tang', 15181001182, '836096399@qq.com', 10025, '发布会未开启'),
        ('limit_full', 1, 'tang', 15181001182, '836096399@qq.com', 10026, '发布会人数限制已满'),
        ('event_over', 3, 'tang', 15181001182, '836096399@qq.com', 10027, '发布会已开始或已结束'),
        ('phone_exist', 2, 'tang', 15181001182, '836096399@qq.com', 10028, '活动嘉宾手机号码重复'),
        ('success', 2, 'tang', 15181001177, '836096399@qq.com', 200, '添加成功'),
    ])
    def test_add_guest_(self, case, eid, realname, phone, email, status, message):
        payload = {'eid':eid,'realname':realname,'phone':phone,'email':email}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

if __name__=="__main__":
    unittest.main()
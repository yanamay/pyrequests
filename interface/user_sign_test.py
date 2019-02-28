import requests
import os,sys
import unittest
from db_fixture import test_data
from parameterized import parameterized
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

class UserSignTest(unittest.TestCase):
    '''用户签到'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/user_sign/"
    def tearDown(self):
        print(self.result)
    @parameterized.expand([
        ('all_null', '', '',10021, '参数不能为空'),
        ('eid_type_err', 'sss', 'aa', 10022, 'eid格式错误'),
        ('phone_type_err', 1, False, 10023, 'phone格式错误'),
        ('query_eid_null', 22, 15181001182,10024, 'Event id为空'),
        ('eid_not_start', 4, 15181001124,10025, '发布会未开启'),
        ('eid_start', 3, 15181001182, 10026, '发布会已开始或已结束'),
        ('user_not_join',2, 15181001132, 10027, '嘉宾未参加发布会'),
        ('has', 1, 15181001122, 10028, '用户已签到'),
        ('success', 1, 15181001121, 200, '签到成功'),

    ])

    def test_user_sign_(self, case, eid, phone,status,message):
        payload = {'eid': eid, 'phone': phone}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"], message)

if __name__=='__main__':
    unittest.main()
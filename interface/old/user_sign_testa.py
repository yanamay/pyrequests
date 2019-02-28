import requests
import os,sys
import unittest
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class UserSignTest(unittest.TestCase):
    '''用户签到'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/user_sign/"
    def tearDown(self):
        print(self.result)
    def test_user_sign_all_null(self):
        '''参数不能为空'''
        payload = {'eid': '', 'phone': ''}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10021)
        self.assertEqual(self.result["message"], "参数不能为空")
    def test_user_sign_eid_type_err(self):
        '''eid类型错误'''
        payload = {'eid': 'sss', 'phone': 'aa'}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10022)
        self.assertEqual(self.result["message"], "eid格式错误")

    def test_user_sign_query_phone_type_err(self):
        '''phone格式错误'''
        payload = {'eid': 1, 'phone': 'sdfsdfsf'}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10023)
        self.assertEqual(self.result["message"], "phone格式错误")

    def test_user_sign_query_eid_null(self):
        '''Event id为空'''
        payload = {'eid': 22, 'phone': 15181001182}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10024)
        self.assertEqual(self.result["message"], "Event id为空")

    def test_user_sign_eid_not_start(self):
        '''发布会未开启'''
        payload = {'eid': 4, 'phone': 15181001124}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10025)
        self.assertEqual(self.result["message"], "发布会未开启")

    def test_user_sign_eid_start(self):
        '''发布会已开始或已结束'''
        payload = {'eid': 3, 'phone': 15181001182}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10026)
        self.assertEqual(self.result["message"], "发布会已开始或已结束")

    def test_user_sign_user_not_join(self):
        '''嘉宾未参加发布会'''
        payload = {'eid': 2, 'phone': 15181001132}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10027)
        self.assertEqual(self.result["message"], "嘉宾未参加发布会")
    def test_user_sign_has(self):
        '''用户已签到'''
        payload = {'eid': 1, 'phone': 15181001122}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10028)
        self.assertEqual(self.result["message"], "用户已签到")
    def test_user_sign_success(self):
        '''签到成功'''
        payload = {'eid': 1, 'phone': 15181001121}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "签到成功")

if __name__=='__main__':
    unittest.main()
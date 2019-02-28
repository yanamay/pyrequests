import requests
import os,sys
import unittest
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class GetEventListTest(unittest.TestCase):
    '''查询嘉宾列表'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/get_guest_list/"
    def tearDown(self):
        print(self.result)
    def test_get_guest_list_all_null(self):
        '''参数不能为空'''
        r = requests.get(self.url, params={'eid':'','phone':''})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10021)
        self.assertEqual(self.result["message"],"参数不能为空")
    def test_get_guest_list_eid_type_err(self):
        '''eid类型错误'''
        r=requests.get(self.url,params={'eid':'ssss'})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10022)
        self.assertEqual(self.result["message"],"eid格式错误")
    def test_get_guest_list_query_eid_null(self):
        '''eid查询结果为空'''
        r=requests.get(self.url,params={'eid':6})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10023)
        self.assertEqual(self.result["message"],"查询结果为空")
    def test_get_guest_list_eid_success(self):
        '''eid成功'''
        r = requests.get(self.url, params={'eid': 1})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"],"成功")
    def test_get_guest_list_query_phone_type_err(self):
        '''phone格式错误'''
        r=requests.get(self.url,params={'eid':1,'phone':'SSSSS'})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10025)
        self.assertEqual(self.result["message"],"phone格式错误")
    def test_get_guest_list_query_phone_null(self):
        '''phone查询结果为空'''
        r=requests.get(self.url,params={'eid':1,'phone':15122119011})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10026)
        self.assertEqual(self.result["message"],"查询结果为空")
    def test_get_guest_list_phone_success(self):
        '''phone成功'''
        r = requests.get(self.url, params={'eid': 1,'phone':15181001121})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"],"成功")

if __name__=="__main__":
    unittest.main()
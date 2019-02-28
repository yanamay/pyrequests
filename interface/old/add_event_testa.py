import requests
import os,sys
import unittest
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/add_event/"
    def tearDown(self):
        print(self.result)
    def test_add_event_all_null(self):
        '''所有参数为空'''
        payload={'eid':'','name':'','limit':'','address':'','start_time':''}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10021)
        self.assertEqual(self.result["message"],"参数不能为空")
    def test_add_event_eid_type_err(self):
        '''eid类型错误'''
        payload={'eid':'ssss','name':'小米5发布会','limit':2,'address':'成都市青羊区','start_time':'2019-02-28 12:0:0'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10022)
        self.assertEqual(self.result["message"],"eid格式错误")
    def test_add_event_limit_type_err(self):
        #limit类型错误
        payload={'eid':1,'name':'小米5发布会','limit':'wwww','address':'成都市青羊区','start_time':'2019-02-28 12:0:0'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10023)
        self.assertEqual(self.result["message"],"limit格式错误")
    def test_add_event_eid_exist(self):
        '''eid已存在'''
        payload = {'eid': 1, 'name': '小米5发布会', 'limit': 2, 'address': '成都市青羊区', 'start_time': '2019-02-28 12:0:0'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10024)
        self.assertEqual(self.result["message"],"eid已存在")
    def test_add_event_name_exist(self):
        '''name已存在'''
        payload = {'eid': 9, 'name': '可添加发布会', 'limit': 2, 'address': '成都市青羊区', 'start_time': '2019-02-28 12:0:0'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10025)
        self.assertEqual(self.result["message"],"name已存在")
    def test_add_event_data_format_err(self):
        '''日期格式错误'''
        payload = {'eid': 9, 'name': '小米9发布会', 'limit': 2, 'address': '成都市青羊区', 'start_time': '2-28 12:0:0'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10026)
        self.assertEqual(self.result["message"],"开始时间格式错误. 必须是YYYY-MM-DD HH:MM:SS格式")
    def test_add_event_success(self):
        '''添加成功'''
        payload = {'eid': 9, 'name': '小米9发布会', 'limit': 2, 'address': '成都市青羊区', 'start_time': '2019-2-28 12:0:0'}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "添加成功")

if __name__=="__main__":
    unittest.main()



import requests
import os,sys
import unittest
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class AddGuestTest(unittest.TestCase):
    '''添加嘉宾'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/add_guest/"
    def tearDown(self):
        print(self.result)
    def test_add_guest_all_null(self):
        '''所有参数为空'''
        payload={'eid':'','realname':'','phone':'','email':''}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10021)
        self.assertEqual(self.result["message"],"参数不能为空")
    def test_add_guest_eid_type_err(self):
        '''eid类型错误'''
        payload={'eid':'sss','realname':'tang','phone':15181001182,'email':'836096399@qq.com'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10022)
        self.assertEqual(self.result["message"],"eid格式错误")
    def test_add_guest_phone_type_err(self):
        '''phone类型错误'''
        payload={'eid':2,'realname':'tang','phone':False,'email':'836096399@qq.com'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10023)
        self.assertEqual(self.result["message"],"phone格式错误")
    def test_add_guest_eid_null(self):
        '''发布会id不存在'''
        payload = {'eid':7,'realname':'tang','phone':15181001127,'email':'836096399@qq.com'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10024)
        self.assertEqual(self.result["message"],"Event id为空")
    def test_add_guest_event_not_start(self):
        '''发布会未开启'''
        payload = {'eid':4,'realname':'yangfan','phone':15181001121,'email':'833396321@qq.com'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10025)
        self.assertEqual(self.result["message"],"发布会未开启")
    def test_add_guest_limit_full(self):
        '''发布会人数限制已满'''
        payload = {'eid':1,'realname':'yangfan','phone':15181001121,'email':'833396321@qq.com'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10026)
        self.assertEqual(self.result["message"],"发布会人数限制已满")
    def test_add_guest_event_over(self):
        '''发布会已开始或已结束'''
        payload = {'eid':3,'realname':'hong','phone':15181001199,'email':'833396344@qq.com'}
        r=requests.post(self.url,data=payload)
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], 10027)
        self.assertEqual(self.result["message"],"发布会已开始或已结束")
    def test_add_guest_phone_exist(self):
        '''活动嘉宾手机号码重复'''
        payload = {'eid': 2, 'realname': 'hong', 'phone': 15181001182, 'email': '833396344@qq.com'}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 10029)
        self.assertEqual(self.result["message"], "活动嘉宾手机号码重复")
    def test_add_guest_success(self):
        '''添加成功'''
        payload = {'eid':2,'realname':'tiandong','phone':15181001177,'email':'8333963321@qq.com'}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], 200)
        self.assertEqual(self.result["message"], "添加成功")

if __name__=="__main__":
    unittest.main()
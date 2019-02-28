import requests
import os,sys
import unittest
from parameterized import parameterized
from db_fixture import test_data
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)

class GetEventListTest(unittest.TestCase):
    '''查询发布会列表'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/get_event_list/"
    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ('all_null', '', '',10021, '参数不能为空'),
        ('eid_type_err', 'ssss', '', 10022, 'eid格式错误'),
        ('query_eid_null', 6, '',10023, '查询结果为空'),
        ('eid_success', 1, '',200, '成功'),
        ('query_name_null', '', 'teteste', 10024, '查询结果为空'),
        ('name_success', '', '可添加发布会', 200, '成功'),
    ])

    def test_get_event_list_(self, case, eid, name,status,message):
        r=requests.get(self.url,params={'eid':eid,'name':name})
        self.result=r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(self.result["status"], status)
        self.assertEqual(self.result["message"],message)
if __name__=="__main__":
    unittest.main()
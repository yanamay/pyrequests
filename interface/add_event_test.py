import requests
import os,sys
import unittest
from parameterized import parameterized
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
    '''添加发布会'''
    def setUp(self):
        self.url="http://127.0.0.1:8000/api/add_event/"
    def tearDown(self):
        print(self.result)
    @parameterized.expand([
        ('all_null','','','','','',10021,'参数不能为空'),
        ('eid_type_err', 'ssss', '小米5发布会', 2, '成都市青羊区', '2019-02-28 12:0:0', 10022, 'eid格式错误'),
        ('limit_type_err', 1, '小米5发布会', 'www', '成都市青羊区', '2019-02-28 12:0:0', 10023, 'limit格式错误'),
        ('eid_exist', 1, '小米5发布会', 2, '成都市青羊区', '2019-02-28 12:0:0', 10024, 'eid已存在'),
        ('name_exist', 9, '可添加发布会', 2, '成都市青羊区', '2019-02-28 12:0:0', 10025, 'name已存在'),
        ('data_format_err', 9, '小米9发布会', 2, '成都市青羊区', '2-28 12:0:0', 10026, '开始时间格式错误'),
        ('event_success', 9, '小米9发布会', 2, '成都市青羊区', '2019-2-28 12:0:0', 200, '添加成功'),
    ])
    def test_add_event_(self,case,eid,name,limit,address,start_time,status,message):
        payload = {'eid': eid, 'name': name, 'limit': limit, 'address': address, 'start_time': start_time}
        r = requests.post(self.url, data=payload)
        self.result = r.json()
        self.assertEqual(r.status_code, 200)
        self.assertEqual(self.result["status"], status)
        if status==10026:
            self.assertIn(message,self.result["message"])
        else:
            self.assertEqual(self.result["message"], message)

if __name__=="__main__":
    unittest.main()



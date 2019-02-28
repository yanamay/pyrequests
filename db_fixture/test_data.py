import sys, time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

past_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()-10000)) #过去时间
future_time=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()+10000)) #未来时间

#create data
datas={
    'sign_event':[
        {'id':1,'name':'限制人数已满','`limit`':2,'status':1,'address':'成都市青羊区','start_time':future_time},
        {'id': 2, 'name': '可添加发布会', '`limit`': 3, 'status': 1, 'address': '成都市高新区', 'start_time': future_time},
        {'id': 3, 'name': '时间已过去', '`limit`': 2, 'status': 1, 'address': '成都市武侯区', 'start_time': past_time},
        {'id': 4, 'name': '状态已关闭', '`limit`': 2, 'status': 0, 'address': '成都市双流县', 'start_time': future_time},
    ],
    'sign_guest':[
        {'realname':'yangfan','phone':15181001121,'email':'833396321@qq.com','sign':0,'event_id':1},
        {'realname': 'may', 'phone': 15181001122, 'email': '833396322@qq.com', 'sign': 1, 'event_id': 1},
        {'realname': 'dong', 'phone': 15181001182, 'email': '833396663@qq.com', 'sign': 0, 'event_id': 2},
        {'realname': 'rose', 'phone': 15181001123, 'email': '833396323@qq.com', 'sign': 0, 'event_id': 3},
        {'realname': 'jack', 'phone': 15181001124, 'email': '833396324@qq.com', 'sign': 0, 'event_id': 4},
    ],
}

# Inster table datas
def test_init_data():
    DB().init_data(datas)


if __name__ == '__main__':
    test_init_data()

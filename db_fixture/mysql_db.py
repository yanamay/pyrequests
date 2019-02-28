import pymysql.cursors
from os.path import abspath, dirname
import configparser as cparser #读取ini后缀的文件

# ======== Reading db_config.ini setting ===========
base_dir = dirname(dirname(abspath(__file__)))
base_dir = base_dir.replace('\\', '/')
file_path = base_dir + "/db_config.ini"

cf=cparser.ConfigParser()
cf.read(file_path)
host=cf.get("mysqlconf","host")
port=cf.get("mysqlconf","port")
db=cf.get("mysqlconf","db_name")
user=cf.get("mysqlconf","user")
password=cf.get("mysqlconf","password")

# ======== MySql base operating ===================
class DB:
    def __init__(self):
        try:
            # Connect to the database
            self.connection = pymysql.connect(host=host,
                                         port=int(port),
                                         user=user,
                                         password=password,
                                         db=db,
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
        except pymysql.err.OperationalError as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))

    # clear table data
    def clear(self,table_name):
        real_sql="delete from "+table_name+";"
        with self.connection.cursor() as cursor:
            cursor.execute("SET FOREIGN_KEY_CHECKS=0;")#取消外键约束
            cursor.execute(real_sql)
        self.connection.commit()
    # insert sql statement
    def insert(self,table_name,table_data):
        for key in table_data:
            table_data[key]="'"+str(table_data[key])+"'"
        key=','.join(table_data.keys())
        value=','.join(table_data.values())
        real_sql="insert into "+table_name+"("+key+")values("+value+")"
        with self.connection.cursor() as cursor:
            cursor.execute(real_sql)
        self.connection.commit()
    # close database
    def close(self):
        self.connection.close()
    #init data
    def init_data(self,datas):
        for table,data in datas.items():
            print(table)
            print(data)
            self.clear(table)
            for d in data:
                self.insert(table,d)
        self.close()

if __name__=="__main__":
    db=DB()
    #db.clear("sign_guest")
    #插入event数据
    #dataevent = {'id':3,'name':'小米6发布会','`limit`':2,'status':1,'address':'成都市青羊区','start_time':'2019-02-28 12:0:0'}
    #db.insert("sign_event", dataevent)
    # 插入guest数据
    #dataguest={'realname':'yangfan','phone':15181001121,'email':'833396321@qq.com','sign':0,'event_id':1}
    #db.insert("sign_guest",dataguest)

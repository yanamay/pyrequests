import sys,time
from db_fixture import test_data
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader

test_dir='./interface'
discover=defaultTestLoader.discover(test_dir,pattern='*_test.py')

if __name__=='__main__':
    test_data.test_init_data() #初始化数据
    #runner=unittest.TextTestRunner()
    #runner.run(discover)
    timestamp = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = './report/' + timestamp + '_result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='发布会管理接口自动化测试用例',
                          description= '运行环境：MySQL(PyMySQL), Requests, unittest')
    runner.run(discover)
    fp.close()

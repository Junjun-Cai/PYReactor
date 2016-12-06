# -*- coding: utf-8 -*
#--------------------------------------------------
# 程序：http_client测试单元
# 作者：ColeCai-蔡君君
# 文件：http_client_test.py
# 日期：2016/10/24-17:24
# 版本：1.0.0
# 环境：python 2.7
# 组件：
# 描述：
# 备注：
#--------------------------------------------------

import sys
sys.path.append("../lib")
from http_client import *

def UnitTest():

    url = 'http://192.168.204.153/gaple/api/gateway.php?&sid=1&lid=2&sesskey=105135-1234567890&debug=39d5800f7ac5d8e2d42f71fbff29a1fd&game_param=%7B%22mid%22:%22%22%7D&method=Chest.getChest'
    url1 = 'http://www.qiushibaike.com//imgrank/'
    myHt = CHttpClient()
    #res = myHt.Connect('192.168.204.153')
    #print res

    res = myHt.Gets(url)
    #print res

    values = {'val1':'123',
              'val2':'abc',
              'val3':'435'}

    headers = {'Connection':'keep-alive',
               'Content-Type':'text/html; charset=utf-8'}

    res = myHt.Posts(url, headers)
    print res
def main():
    args = sys.argv
    UnitTest()

if __name__ == '__main__':
    print 'sys.args = ' + __name__
    print sys.argv
    main()

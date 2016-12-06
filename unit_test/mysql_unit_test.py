# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：mysql_client测试单元。
# 作者：ColeCai-蔡君君
# 文件：mysql_unit_test.py
# 日期：2016/10/9-11:20
# 版本：1.0.0
# 环境：python 2.7
# 组件：
# 描述：
# 备注：
#-------------------------------------------------------

import sys
import logging
sys.path.append("../lib")
from mysql_client import *

HOST = '192.168.204.153'
USER = 'root'
PWD = ''
DBNAME = 'gaple_friends'
DBNAME2 = 'gaple'
PORT = 3388


def UnitTest():
    print "UnitTest MySQL Connect!!"

    myConn = CMySql()
    myConn.Connect(HOST, USER, PWD, DBNAME, PORT)
    Uid = 105044
    result = []

    # 切换数据库
    print "chang database!!!"
    cnt = myConn.ChangeDatabase('gaple')
    print cnt

    # 切换数据库
    print "change database !!!"
    res = myConn.ChangeDatabase('python_text')
    print res

    # 插入一条记录
    print "insert one record !!!"
    sql = 'insert into userdata values(%s, %s, %s, %s, %s)'
    val = [105044, 20000000, 4000, 50, 30]
    cnt = myConn.Insert(sql, val)  # cnt,受影响的行数，失败为0
    result = myConn.SelectAll('select * from userdata')
    print result
    print cnt

    # 删除记录
    print "delete record !!!"
    sql = 'delete from userdata where mid = 105044'
    myConn.Delete(sql)
    result = myConn.SelectAll('select * from userdata')
    print result

    # 插入多条记录
    print "insert many records !!!"
    sql = 'insert into userdata values(%s, %s, %s, %s, %s)'
    vals = []
    vals.append((105044, 20000000, 4000, 50, 30))
    vals.append((105045, 30000000, 5000, 60, 40))
    vals.append((105046, 40000000, 6000, 70, 50))
    vals.append((105047, 50000000, 7000, 80, 60))
    cnt = myConn.InsertMany(sql, vals)  # cnt,受影响的行数，插入失败则为0
    result = myConn.SelectAll('select * from userdata')
    print result
    print cnt
    sql = 'delete from userdata where mid > 0'
    res = myConn.Delete(sql)
    print res


def main():
    args = sys.argv
    UnitTest()


if __name__ == '__main__':
    print ' sys.argv= ' + __name__
    print sys.argv
    logging.warning('call main FFF')
    main()
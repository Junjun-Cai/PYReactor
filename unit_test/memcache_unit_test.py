# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：memcache_client测试单元。
# 作者：ColeCai-蔡君君
# 文件：memcache_unit_test.py
# 日期：2016/10/10-17:21
# 版本：1.0.0
# 环境：python 2.7
# 组件：
# 描述：
# 备注：
#-------------------------------------------------------

import sys
import logging
sys.path.append("../lib")
from memcached_client import *

LIST = ["192.168.204.153:11200"]

def UnitTest():
    myMem = CMemecachedClient()
    print "Unitest memcache connect !!!"
    print "\nconnect to memcache !!!"
    res = myMem.Connect(LIST)
    print res

    print "\nset key-value !!!"
    #设置键值对
    res = myMem.Set('mem1', 6 ,5)
    print res

    print "\nget value !!!"
    #根据键获取值
    res= myMem.Get('mem1')
    print res

    print "\nset multi key-value !!!"
    #设置多个键值
    data = {'mem2':6, 'mem3':3, 'mem4':4}
    res = myMem.SetMulti(data)
    print res

    print "\nadd key-value !!!"
    #添加一个键值对
    res = myMem.Add('memx', 5)
    print res

    print "\nreplace value !!!"
    #替换value
    res = myMem.Replace('mem5', 1000)
    print res

    print "\nincr value !!!"
    #自增运算
    res = myMem.Incr('mem2', 10)
    print res

    print "\ndecr value !!!"
    #自减运算
    res = myMem.Decr('mem2', 10)
    print res

    print "\nget value multi !!!"
    # 获取多个key的值
    keys = ['mem1', 'mem2', 'mem3', 'mem4', 'mem5']
    res = myMem.GetMulti(keys)
    print res
    keys = ['1', '2', '3', '4', '5']
    prefix_key = 'mem'
    res = myMem.GetMulti(keys, prefix_key)
    print res

    print "\ndelete key !!!"
    #删除指定的key
    res = myMem.Delete('mem3')
    print res

def main():
    args = sys.argv
    UnitTest()

if __name__ == '__main__':
    print ' sys.argv= ' +__name__
    print sys.argv
    logging.warning('call mian FFF')
    main()


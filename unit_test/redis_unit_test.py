# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：redis_client测试单元。
# 作者：ColeCai-蔡君君
# 文件：redis.py
# 日期：2016/10/8-15:04
# 版本：1.0.0
# 环境：python 2.7
# 组件：
# 描述：
# 备注：
#-------------------------------------------------------

import sys
import logging
import time
sys.path.append("../lib")
from redis_client import *


HOST = '192.168.204.153'
PORT = 4500
HASH = 'python_redis_test'
NEWHASH = 'python_redis_hash'
SET = 'python_redis_set'
LIST = 'python_redis_list'
STRING = 'python_redis_string'

def UnitTest():
    print "Unittest Redis Connect!!"

    print "\nconnect to redis !!!"
    myRed = CRedisClient()
    res = myRed.Connect(HOST, PORT)
    print res
    #time.sleep(10)

    print "\ninsert into hash !!!"
    #向map中插入一条数据
    res = myRed.Hset(HASH, 'uid', 105044)
    print res

    print "\nget from hash !!!"
    #从map中取出一条数据
    res = myRed.Hget(HASH,'uid')
    print res

    print "\ninsert into hash many !!!"
    #批量更新map中的键值对
    data = {}
    data['exp'] = 5000
    data['money'] = 30000000000
    data['win'] = 50
    data['lose'] = 20
    res = myRed.Hmset(HASH, data)
    print res

    print "\nget from hash all key_value !!!"
    #从map中取出所有的键值对
    res = myRed.Hgetall(HASH)
    print len(res)

    print "\nget from hash all value !!!"
    #批量从map中取出指定域的值
    fields = ['uid', 'exp', 'mondey', 'win', 'lose']
    res = myRed.Hmget(HASH, fields)
    print res

    print "\ndelete field !!!"
    #删除map的指定域
    res = myRed.Hdel(HASH, 'uid')
    print res

    print "\nget from hash all field !!!"
    #获取指定key的所有域
    res = myRed.Hkeys(HASH)
    print res

    print "\nrename hash key !!!"
    #对指定的key进行重命名操作
    res = myRed.Rename(HASH, NEWHASH)
    print res

    print "\ninsert memebers into set !!!"
    #将给定的member元素加入的集合set中
    res = myRed.Sadd(HASH, 100000, 245234, 5134515)
    print res

    print "\nget all members from set !!!"
    #获取集合set中的所有元素
    res = myRed.Smembers(SET)
    print res

    print "\ninsert into list tail !!!"
    #向列表list尾部插入元素
    res = myRed.Rpush(LIST, 80000, 7000, 3000, 2222)
    print res

    print "\nget list length !!!"
    #获取列表list的长度
    res = myRed.Llen(LIST)
    print res

    print "\nget and move from list head !!!"
    #移除并返回列表key的头元素
    res = myRed.Lpop(LIST)
    print res

    print "\nstring get !!!"
    #获取key的值
    res = myRed.Get(HASH)
    print res

    print "\nstring set !!!"
    #设置key的值
    res = myRed.Set(STRING,'dsd')
    print res

    print "\nstring get !!!"
    # 获取key的值
    res = myRed.Get(STRING)
    print res

    print "\nstring incr !!!"
    #指定string进行自增长
    res = myRed.Incr('ddd')
    print res

    print "\nstring decr !!!"
    # 指定string进行自减运算。
    res = myRed.Decr('ddd')
    print res

    print "\nset life time !!!"
    #为给定的key设置生存时间,成功返回True，失败返回False
    res = myRed.Expire(SET, 300)
    print res

    print "\nkey is exists !!!"
    #检查给定key是否存在,成功返回True，失败返回False
    res = myRed.Exists('sd57')
    print res

    print "\nget life time !!!"
    #获取给定key的剩余生存时间，单位秒
    res = myRed.Ttl(SET)
    print res


    va = None

    print 'xxx',str(va)+'2'
def main():
    args = sys.argv
    UnitTest()

if __name__ == '__main__':
    print ' sys.argv= ' +__name__
    print sys.argv
    logging.warning('call main FFF')
    main()


# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：连接memcache，并操作数据。
# 作者：ColeCai-蔡君君
# 文件：memcached_client.py
# 日期：2016/10/10-15:59
# 版本：1.0.0
# 环境：python 2.7
# 组件：memcache
# 描述：连接memcache，对数据进行增、删、改、查等操作。
# 备注：
#   1、连接memcache服务器的ip和端口以list的形式传参，例如：
# ["192.168.204.153:11200"]
#-------------------------------------------------------

import memcache
import sys
sys.path.append("../core")
from const import *

const.OPERATE_SUCCESS = 1
const.OPERATE_FAILURE = -1
class CMemecachedClient():

    def __init__(self):
        self.mem = None

    def Connect(self, list):
        """
        @summary:连接memcache。
        @param list: memcache的端口及地址组成的list。
        @return:操作成功则返回1，否则返回-1。
        """
        try:
            self.mem = memcache.Client(list)
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def Set(self, key, value, time=0, min_compress_len=0):
        """
        @summary:设置键值对。
        @param key：键。
        @param value: 值。
        @param time: 超时时间，单位秒,默认为0，即该项永不过期，若为非0，到达超时时间后，客户端无法再获得这项内容。
        @param min_compress_len: 设置zlib压缩。
        @return:操作成功返回1，否则返回-1。
        """
        try:
            return self.mem.set(key, value, time, min_compress_len)
        except:
            return const.OPERATE_FAILURE

    def Get(self, key):
        """
        @summary:根据key获取value。
        @param key: 键。
        @return: 操作成功返回获取到的值，否则返回-1。
        """
        try:
            return self.mem.get(key)
        except:
            return const.OPERATE_FAILURE

    def SetMulti(self, mapping, time=0, key_prefix='', min_compress_len=0):
        """
        @summary:设置多对键值。
        @param mapping: 键值对的字典。
        @param time: 超时时间，单位秒,默认为0，即该项永不过期，若为非0，到达种植时间后，客户端无法再获得这项内容。
        @param key_prefix: key的前缀。
        @param min_compress_len: 设置zlib压缩。
        @return:设置成功返回1，否则返回-1。
        """
        try:
            self.mem.set_multi(mapping, time, key_prefix, min_compress_len)
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def Add(self, key, value, time=0, min_compress_len=0):
        """
        @summary:添加一个键值对。
        @param key: 键。
        @param value: 值。
        @param time: 超时时间，单位秒,默认为0，即该项永不过期，若为非0，到达种植时间后，客户端无法再获得这项内容。
        @param min_compress_len: 设置zlib压缩。
        @return:添加成功返回1, 否则返回-1。
        """
        try:
            return self.mem.add(key, value, time, min_compress_len)
        except:
            return const.OPERATE_FAILURE

    def Replace(self, key, value, time=0, min_compress_len=0):
        """
        @summary:替换value的值。
        @param key: 键。
        @param value: 替换后的值。
        @param time: 超时时间，单位秒,默认为0，即该项永不过期，若为非0，到达种植时间后，客户端无法再获得这项内容。
        @param min_compress_len: 设置zlib压缩。
        @return:替换成功返回1，键不存在返回-1。
        """
        try:
            return self.mem.replace(key, value, time, min_compress_len)
        except:
            return const.OPERATE_FAILURE

    def GetMulti(self, keys, key_prefix=''):
        """
        @summary:获取多个key的值。
        @param keys: key的列表。
        @param key_prefix: key的前缀。
        @return: 操作成功则返回获取到的值，字典类型,否则返回-1。
        """
        try:
            return self.mem.get_multi(keys, key_prefix)
        except:
            return const.OPERATE_FAILURE

    def Incr(self, key, delta=1):
        """
        @summary:对key的值进行自增运算。
        @param key:键。
        @param delta:每次自增的量，默认为1.
        @return:操作成功返回自增之后的值，否则返回-1。
        """
        try:
            return self.mem.incr(key, delta)
        except:
            return const.OPERATE_FAILURE

    def Decr(self, key, delta=1):
        """
        @summary:自减运算。
        @param key:键。
        @param delta:每次自减的量，默认为1，
        @return：操作成功返回自减之后的值，否则返回-1。
        """
        try:
            return self.mem.decr(key, delta)
        except:
            return const.OPERATE_FAILURE

    def Delete(self, key, time=0):
        """
        @summary:删除key。
        @param key:键。
        @param time：用于确保在特定时间内的set和update操作会失败。
        @return:操作成功返回1，否则返回-1。
        """
        try:
            self.mem.delete(key)
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE
# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：redis_client。
# 作者：ColeCai-蔡君君
# 文件：redis.py
# 日期：2016/10/8-15:04
# 版本：1.0.0
# 环境：python 2.7
# 组件：redis
# 描述：连接redis，对redis进行常规操作。
# 备注：所有的返回值都将以(CODE, RET)的形式返回，CODE有两种取值分别是1和-1，
#只有当CODE=1，RET才有实际意义, CODE=-1时，RET=False。
#-------------------------------------------------------

import redis
import sys
sys.path.append("../core")
from const import *

const.ERROR_VALUE = -1
const.VALI_VALUE = 1

class CRedisClient(object):

    def __init__(self):
        self.red = None

    def Connect(self, host, port):
        """
        @summary:连接redis。
        @param host:需要进行连接的redis的IP地址。
        @param port:redis的端口。
        @return:result, 连接成功则返回(1, True)，否则返回(-1, False)。
        """
        try:
            self.red = redis.Redis(host, port)
            return (const.VALI_VALUE, True)
        except:
            return (const.ERROR_VALUE, False)

    def Set(self, key, value):
        """
        @summary:将字符串value关联到key，如果key已经持有其他值，set就覆盖旧值，无视类型
        @param key:指定key。
        @param value:指定值。
        @return:操作成功返回(1, True),否则返回(-1, False)。
        """
        try:
            ret = self.red.set(key, value)
            if ret is True:
                return (const.VALI_VALUE, True)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Get(self, key):
        """
        @summary:返回key所关联的字符串值。
        @param key:指定key。
        @return:操作成功则返回key的值(1, ret)，否则返回(-1, False)。
        """
        try:
            ret = self.red.get(key)
            if ret is not None:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Hset(self, key, field,  value):
        """
        @summary:向哈希表key中域field的值设为value，如果key不存在则会新建一个哈希表，并进行Hset操作，如果field已经存在，旧值会被覆盖。
        @param key:哈希表。
        @param field:指定域。
        @param value:值。
        @return:若field是一个新建域，并且值设置成功则返回(1,1)，若field已经存在并且新值将旧值覆盖则返回(1, 0)，否则返回(-1, False)。
        """
        try:
            ret = self.red.hset(key, field, value)
            return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)

    def Hget(self, key, field):
        """
        @summary:获取哈希表key中给定域的值。
        @param key:哈希表。
        @param field:指定域名称。
        @return:获取成功返回指定域的值(1, ret)，否则返回(-1, False)。
        """
        try:
             ret = self.red.hget(key, field)
             if ret is not None:
                 return (const.VALI_VALUE, ret)
             else:
                 return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Hkeys(self,key):
        """
        @summary:返回哈希表 key 中的所有域。
        @param key:进行操作的哈希表key。
        @return:获取成功返回获取到的结果(1, ret)，列表类型，否则返回(-1, False)。
        """
        try:
             ret = self.red.hkeys(key)
             if ret is not None:
                 return (const.VALI_VALUE, ret)
             else:
                 return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Hdel(self, key, *args):
        """
        @summary: 删除哈希表key的一个或多个指定域，不存在的域将被忽略。
        @:param name: 需要进行移除操作的哈希表key。
        @:param args: 需要删除的域，不定长个数。
        @:return:成功返回移除的域的数量(1, ret),若域不存在将返回(-1, False)。
        """
        try:
            ret = self.red.hdel(key, *args)
            if ret > 0:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Hmset(self, key, datas):
        """
        @summary: 批量更新数据，没有则新建。
        @:param key: 需要进行更新的数据。
        @:param datas: 更新后的值,字典类型。
        @:return:成功返回(1, True),否则返回(-1, False)。当key不是哈希表类型时也将返回(-1, False)。
        """
        try:
            ret = self.red.hmset(key,datas)
            if ret is True:
                return (const.VALI_VALUE, True)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Hmget(self, key, fields):
        """
        @summary:返回哈希表 key 中，一个或多个给定域的值。
        @param key:哈希表。
        @param fields:域的列表，list类型。
        @return:获取成功则返回获取到的值(1, ret)，ret为列表类型，否则返回(-1, False)。
        """
        try:
            ret = self.red.hmget(key, fields)
            return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)

    def Hgetall(self, name):
        """
        @summary: 获取这条数据的所有属性和对应的值。
        @:param name: 续要进行查询的数据。
        @:return: 获取成功则返回查询结果(1, ret)，ret为字典类型，否则返回(-1, False)。若hash表不存在也将返回(-1, False)。
        """
        try:
            ret = self.red.hgetall(name)
            if len(ret) > 0:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Incr(self, name):
        """
        @sumary:自增长。
        @param name:进行自增长的key。
        @return:自增长运算成功则返回执行一次自增长之后的值(1, ret)，否则返回(-1, False)。
        如果key不存在，那么key的值会先被初始化为0 ，然后再执行INCR操作。
        """
        try:
            ret = self.red.incr(name)
            return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)

    def Decr(self, name):
        """
        @summary:自减少。
        @param name:进行自增长的key。
        @return:自减运算成功则返回执行一次自减少之后的值(1, ret)，否则返回(-1, False)。
        如果key不存在，那么key的值会先被初始化为0，然后再执行DECR操作。
        """

        try:
            ret = self.red.decr(name)
            return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)

    def Rpush(self, key, *args):
        """
        @summary:将value插入列表key的表尾。
        @:param key:需要操作的列表。
        @:param args:需要插入的值，不定长个数。
        @:return:插入成功则返回列表当前的长度(1, ret)，否则返回(-1, False)。
                 如果key不存在，一个空列表会被创建并执行RPUSH操作。
                 当key存在但不是列表类型时，返回(-1, False)。
        """
        try:
            ret =  self.red.rpush(key, *args)
            if ret is not False:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Lpop(self, key):
        """
        @summary:移除并返回列表key的头元素。
        @param key:需要进行操作的列表。
        @return:操作成功则返回列表的头元素(1, ret)，否则返回(-1, False)。当key不存在时也将返回(-1, False)
        """
        try:
            ret = self.red.lpop(key)
            if ret is not None:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Llen(self, key):
        """
        @summary:获取列表key的长度。
        @param key: 列表名。
        @return:操作成功则返回len长度(1, ret)，否则返回(-1, False)。
                如果key不存在，则key被解释为一个空列表，返回(1, 0)。
                如果key不是列表类型，返回(-1, False)。
        """
        try:
            ret = self.red.llen(key)
            if ret is not False:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Ttl(self, key):
        """
        @summary:以秒为单位，返回给定key的剩余生存时间。
        @param key: 表名。
        @return: 操作成功则返回剩余生存时间(1, ret)，单位秒，否则返回(-1, False)。
                 当key不存在时或者当key存在但没有设置剩余生存时间时也将返回(-1, False)。
        """
        try:
            ret = self.red.ttl(key)
            if ret >= 0:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Del(self, *args):
        """
        @summary:删除给定的key。
        @param args:需要删除的key名，不定长个数。
        @return:操作成功则返回被删除key的数量(1, ret)，否则返回(-1, False)。
                key不存在时返回(1, 0)。
        """
        try:
            ret = self.red.hdel(*args)
            return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)

    def Expire(self, key, seconds):
        """
        @summary:为给定key设置生存时间，当key过期时(生存时间为 0 )，它会被自动删除。
        @param key:
        @param seconds:设置的生存时间，单位秒。
        @return:设置成功返回true(1, True), 失败返回(-1, False)。
                当key不存在或者不能为key设置生存时间时也将返回(-1, False)。
        """
        try:
            ret = self.red.expire(key, seconds)
            if ret > 0:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Exists(self, key):
        """
        @summary:检查给定key是否存在。
        @param key:给定的key。
        @return:key存在返回(1, True)，不存在返回(-1, False),发生其他错误返回(-1, False)。
        """
        try:
            ret = self.red.exists(key)
            if ret is not False:
                return (const.VALI_VALUE, ret)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Srem(self, key, *args):
        """
        @summary:移除集合key给定的member元素，不存在的member元素会被忽略。
        @param key:需要进行操作的set。
        @param args:需要移除的元素，不定长个数。
        @return:操作成功则返回成功移除的元素数量(1, ret)，不包括被忽略的元素，否则返回(-1, False)。
                当key不是集合类型，返回(-1, False).
        """
        try:
            ret = self.red.srem(key, *args)
            if ret is False:
                return (const.ERROR_VALUE, False)
            else:
                return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)

    def Sadd(self, key, *args):
        """
        @summary:将给定的 member 元素加入到集合 key 当中，已经存在于集合的member元素将被忽略。
        @param key:需要进行操作的set。
        @param args:需要插入set的元素，不定长个数。
        @return:操作成功则返回被添加到集合中的新元素数量(1, ret)，不包括被忽略的元素，否则返回(-1, False)。
                假如key不存在，则创建一个只包含member元素作成员的集合。返回值为元素个数(1, ret)。
                当key不是集合类型时将返回(-1, False)。
        """
        try:
            ret = self.red.sadd(key, *args)
            if ret is False:
                return (const.ERROR_VALUE, False)
            else:
                return (const.ERROR_VALUE, False)
        except:
            return (const.ERROR_VALUE, False)

    def Smembers(self, key):
        """
        @summary:返回集合中所有元素。
        @param key:指定集合。
        @return：操作成功则返回集合中所有元素(1, ret)，不存在的集合被视为空集合，否则返回(-1, False)。
        """
        try:
            ret = self.red.smembers(key)
            return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)

    def Rename(self, key, newkey):
        """
        @summary:对key进行重命名操作
        @param key:原始key。
        @param newkey:新的key名。
        @return:操作成功则返回(1,True)，否则返回(-1, False)。
                当key和newkey相同，或者key不存在时，返回(-1, False)。
                当newkey已经存在时，会用key来覆盖newkey。
        """
        try:
            ret = self.red.rename(key, newkey)
            if ret is False:
                return (const.ERROR_VALUE, False)
            else:
                return (const.VALI_VALUE, ret)
        except:
            return (const.ERROR_VALUE, False)
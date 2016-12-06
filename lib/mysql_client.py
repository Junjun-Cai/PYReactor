# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：mysql_client。
# 作者：ColeCai-蔡君君
# 文件：mysql_client.py
# 日期：2016/9/30-11:47
# 版本：1.0.0
# 环境：python 2.7
# 组件：MySQLdb
# 描述：实现对MySQL数据库的连接、增、删、改、查等操作。
# 备注：
#   1、antocommit自动提交只有在支持事物类型的数据表才会起作用。
#-------------------------------------------------------

import MySQLdb
import sys
from MySQLdb.cursors import DictCursor
sys.path.append("../core")
from const import *

const.OPERATE_SUCCESS = 1
const.OPERATE_FAILURE = -1

class CMySql(object):

    def __init__(self):
        self.conn = None
        self.cur = None

    def __del__(self):
        self.Destory()

    def Connect(self, host, port, user, passwd, dbname):
        """
        @summary:连接数据库.
        @param host: 数据库的IP地址.
        @param port: 数据库的端口.
        @param user: 用户名.
        @param passwd: 密码.
        @param dbname: 数据库名称.
        @return: 连接成功返回1，否则返回-1.
        """
        try:
            self.conn = MySQLdb.connect(host, port, user, passwd, dbname)
            self.cur = self.conn.cursor()
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def Query(self, sql, param=None):
        """
        @summary:执行sql语句.
        @param sql: 需要执行的sql语句.
        @param param: 可选参数，条件列表值(元组/列表).
        @return: 操作成功则受影响的行数，否则返回-1.
        """
        try:
            if param is None:
                count = self.cur.execute(sql)
            else:
                count = self.cur.execute(sql, param)
            return count
        except:
            return const.OPERATE_FAILURE

    def Insert(self, sql, value):
        """
        @summary:向数据表插入1条记录.
        @param sql:要插入的SQL格式.
        @param value:要查入得记录数据tuple/list.
        @return:操作成功则受影响的行数，否则返回-1.
        """
        try:
            count = self.cur.execute(sql,value)
            self.conn.commit()
            return count
        except:
            return const.OPERATE_FAILURE

    def InsertMany(self, sql, values):
        """
        @summary：向数据表插入多条记录.
        @param sql: 要插入的SQL格式.
        @param values: 要插入的数据tuple/list.
        @return:操作成功则受影响的行数，否则返回-1.
        """
        try:
            count = self.cur.executemany(sql, values)
            self.conn.commit()
            return count
        except:
            return const.OPERATE_FAILURE

    def Delete(self, sql, param=None):
        """
        @summary:删除数据表记录
        @param sql: SQL格式及条件，使用（%s,%s）
        @param param: 要删除的条件，tuple/list
        @return:操作成功则受影响的行数，否则返回-1.
        """
        try:
            return self.Query(sql, param)
        except:
            return const.OPERATE_FAILURE

    def Update(self, sql, param=None):
        """
        @summary:更新数据表记录
        @param sql:SQL格式及条件，使用(%s,%s)
        @param param: 要更新的值，tuple/list
        @return:操作成功则受影响的行数，否则返回-1.
        """
        try:
            return self.Query(sql, param)
        except:
            return const.OPERATE_FAILURE

    def SelectAll(self, sql, param=None):
        """
        @summary:执行查询，并取出所有结果集.
        @param sql:查询SQL,如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来.
        @param param:可选参数，条件列表值(元组/列表).
        @return:操作成功则返回查询到的结果集(list类型),否则返回-1.
        """
        try:
            count = self.Query(sql, param)
            if count > 0:
                result = self.cur.fetchall()
            else:
                result = False
            return result
        except:
            return const.OPERATE_FAILURE

    def SelectOne(self, sql, param=None):
        """
        @summary:执行查询，并取出第一条.
        @param sql: 查询SQL,如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来.
        @param param: 可选参数，条件列表值(元组/列表).
        @return:操作成功则返回查询到的结果集(list类型),否则返回-1.
        """
        try:
            count = self.Query(sql, param)
            if count > 0:
                result = self.cur.fetchone()
            else:
                result = False
            return result
        except:
            return const.OPERATE_FAILURE

    def SelectNum(self, sql, num, param=None):
        """
        @summary:执行查询，并取出num调结果.
        @param sql: 查询SQL,如果有查询条件，请指定条件列表，并将条件值使用参数[param]传递进来.
        @param num: 取得的结果的条数.
        @param param: 可选参数，条件列表值(元组/列表).
        @return:操作成功则返回查询到的结果集(list类型),否则返回-1.
        """
        try:
            count = self.Query(sql, param)
            if count > 0:
                result = self.cur.fetchmany(num)
            else:
                result = False
            return result
        except:
            return const.OPERATE_FAILURE

    def OpenCommit(self):
        """
        @summary:开启事物,设置自动提交.
        @return:操作成功返回1，否则返回-1.
        """
        try:
            self.conn.autocommit(1)
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def CloseCommit(self, option='commit'):
        """
        @summary:关闭事物，关闭自动提交.
        @return:操作成功返回1，否则返回-1.
        """
        try:
            self.conn.autocommit(0)
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def Rollback(self):
        """
        @summary:回滚.
        @return:操作成功返回1，否则返回-1.
        """
        try:
            self.conn.rollback()
            return const.OPERATE_FAILURE
        except:
            return const.OPERATE_SUCCESS

    def Destory(self):
        """
        @summary:提交事务，关闭连接.
        @return:操作成功返回1，否则返回-1.
        """
        try:
            self.conn.commit()
            self.cur.close()
            self.conn.close()
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def ChangeDatabase(self, dbname):
        """
        @summary:切换数据库.
        @param dbname:数据库名.
        @return:操作成功返回1，否则返回-1.
        """
        try:
            sql = 'use ' + dbname
            self.Query(sql)
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE
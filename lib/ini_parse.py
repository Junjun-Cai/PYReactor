# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：解析.ini文件。
# 作者：ColeCai-蔡君君
# 文件：ini_parse.py
# 日期：2016/10/13-12:04
# 版本：1.0.0
# 环境：python 2.7
# 组件：ConfigParser
# 描述：程序用于加载ini文件并进行解析，可以获取ini文件下的所有节点、
# 某一个节点下的所有属性及属性值、某一个节点下某一项指定属性的值。
# 备注：
#   1、获取到的值都是str类型，需要对获取结果进行相应的类型转换。
#-------------------------------------------------------


import ConfigParser
import sys
sys.path.append("../core")
from const import *

const.OPERATE_SUCCESS = 1
const.OPERATE_FAILURE = -1
class CIniParse(object):

    def __init__(self):
        self.reader = None

    def LoadIniFile(self, filename):
        """
        @summary:打开ini文件。
        @param filename: 文件名。
        @return: 操作成功则返回1，否则返回-1。
        """
        try:
            self.reader = ConfigParser.RawConfigParser()
            self.reader.read(filename)
            return const.OPERATE_SUCCESS
        except:
            return const.OPERATE_FAILURE

    def GetAllSection(self):
        """
        @summary:获取所有的section。
        @return:操作成功则返回获取到的section，返回值类型：list，操作失败则返回-1。
        """
        try:
            return self.reader.sections()
        except:
            return const.OPERATE_FAILURE

    def GetAllItems(self, section_name):
        """
        @summary:获取某一个section下所有的属性及属性的值。
        @param section_name:需要获取属性的section。
        @return:操作成功则返回获取到的section，返回值类型：list，操作失败则返回-1。
        """
        try:
            return self.reader.items(section_name)
        except:
            return const.OPERATE_FAILURE

    def GetAttribValue(self, section_name, attrib_name):
        """
        @summary:获取某一个section下某一项属性的值。
        @param section_name: 获取值的属性所属的section。
        @param attrib_name: 获取值的属性。
        @return:操作成功则返回获取到的值，返回值类型：str，否则返回-1。
        """
        try:
            return self.reader.get(section_name, attrib_name)
        except:
            return const.OPERATE_FAILURE
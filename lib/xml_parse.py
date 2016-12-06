# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：xml文件的加载和解析。
# 作者：ColeCai-蔡君君
# 文件：xml_parse.py
# 日期：2016/10/12-9:38
# 版本：1.0.0
# 环境：python 2.7
# 组件：ElementTree
# 描述：获取xml文件中的标记的属性及属性值以及其标记内容。
# 备注：
#   1、python提供的xml处理模块不支持gb2312编码，所以在打开
# gb2312编码的xml文件之前需要对文件进行转码，否则打开文件就会
# 出错。
#   2、ElementTree在python标准库中有两种实现：一种是纯Python
# 实现的，如xml.etree.ElementTree，另一种是速度快一点的
# xml.etree.cElementTree。cElementTree是使用c语言实现的，所
# 以它的数度更快而且消耗的内存少。
#-------------------------------------------------------

try:
    import  xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import sys
sys.path.append("../core")
from const import *

const.ERROR_VALUE = -1
const.VALI_VALUE = 1
class CXmlParse(object):

    def __init__(self):
        self.tree = None
        self.root = None
        self.nodes = None

    def LoadXmlFile(self, filename):
        """
        @summary:打开.xml文件。
        @param filename: 文件名。
        @return:操作成功则返回1,否则返回-1。
        """
        try:
            self.tree = ET.parse(filename)
            self.root = self.tree.getroot()
            self.nodes = self.root

            return const.VALI_VALUE
        except:
            return const.ERROR_VALUE

    def FindAssignLabel(self, elem):
        """
        @summary:寻找指定的标记。
        @param elem: 标记名，可以是嵌套标记，如：'Root/Node/Child',Root是根节点，Child是最内层节点，Root、Node、Child是父子关系。
        @return:操作成功则返回节点，否则返回-1, 若节点不存在也会返回-1
        """
        try:
            self.nodes = self.root.findall(elem)
            if len(self.nodes) <= 0:
                return (const.ERROR_VALUE, False)
            else:
                return (const.VALI_VALUE, self.nodes)
        except:
            return (const.ERROR_VALUE, False)


    def GetLabelValue(self):
        """
        @summary:获取节点下所有属性以及值。
        @return:操作成功则返回获取到的属性以及值，list类型，其中的元素为属性：值的字典类型,否则返回-1。
        """
        values = []
        try:
            for node in self.nodes:
                values.append(node.attrib)
            if len(values[0]) <= 0:
                return (const.ERROR_VALUE, False)
            else:
                return (const.VALI_VALUE, values)
        except:
            return (const.ERROR_VALUE, False)

    def GetLabelAttribute(self, attrname):
        """
        @summary:获取某个标记某一项属性的值，如：<Server svid="1" ip="192.168.204.153" port="4435"/>中的svid的值。
        @param attrname:属性名。
        @return:操作成功则返回获取到的值(list类型)，操作失败则返回-1。若标记下没有该属性也将返回-1。
        """
        values = []
        try:
            for node in self.nodes:
                values.append(node.get(attrname))
            if len(values) == 1 and values[0] is None:
                return (const.ERROR_VALUE, False)
            else:
                return (const.VALI_VALUE, values)
        except:
            return (const.ERROR_VALUE, False)

    def GetLabelContent(self, labelname):
        """
        @summary:获取某个标记的内容。如：<rank>43434</rank>中的43434。
        @param contentname:标记名。
        @return:操作成功则返回获取到的结果(list类型),操作失败则返回-1。若没有该标记也将返回-1。
        """
        values = []
        try:
            for node in self.nodes:
                nodes = node.findall(labelname)
                for no in nodes:
                    values.append(no.text)
            if len(values) <= 0:
                return (const.ERROR_VALUE, False)
            else:
                return (const.VALI_VALUE, values)
        except:
            return (const.ERROR_VALUE, False)


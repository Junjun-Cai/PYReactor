# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：xml文件的加载和解析单元测试。
# 作者：ColeCai-蔡君君
# 文件：xml_unit_test.py
# 日期：2016/10/12-11:46
# 版本：1.0.0
# 环境：python 2.7
# 组件：ElementTree
# 描述：
# 备注：
#-------------------------------------------------------

import sys
import logging
sys.path.append("../lib")
from xml_parse import *

XMLFILE = 'xml_test.xml'

def UnitTest():
    print 'xml parse unittest !!!'
    myXml = CXmlParse()

    print 'load xml file !!!'
    root = myXml.LoadXmlFile(XMLFILE)
    print root

    print  'get element !!!'
    res = myXml.FindAssignLabel('Node/test/test1')
    print res

    print 'get value len!!!'
    res = myXml.GetLabelValue()
    print res
    print len(res)

    print 'get element server flag !!!'
    res = myXml.FindAssignLabel('Node/AllocServer/Server')
    print res

    print 'get value!!!'
    res = myXml.GetLabelValue()
    print res

    print 'get element flag !!!'
    res = myXml.FindAssignLabel('Node/Flag/Friend')
    print res

    print 'get friend value!!!'
    res = myXml.GetLabelValue()
    print res

    print 'get element flag !!!'
    res = myXml.FindAssignLabel('Node/BroadcastServer/Server')
    print res

    print 'get attr svid'
    res = myXml.GetLabelAttribute('svid')
    print res
    print len(res)

    print  'get element !!!'
    res = myXml.FindAssignLabel('Node/mt_redis')
    print res

    print 'get attr'
    res = myXml.GetLabelAttribute('ip')
    print res

    print 'get element flag !!!'
    res = myXml.FindAssignLabel('Node/Test')
    print res

    print 'get value!!!'
    res = myXml.GetLabelContent('rank')
    print res
    print len(res)


def main():
    args = sys.argv
    UnitTest()

if __name__ == '__main__':
    print 'sys.args = ' + __name__
    print sys.argv
    #logging.warning('call mian FFF')
    main()



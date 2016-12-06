# -*- coding: utf-8 -*
#-------------------------------------------------------
# 程序：解析.ini文件单元测试。
# 作者：ColeCai-蔡君君
# 文件：ini_unit_test.py
# 日期：2016/10/13-12:23
# 版本：1.0.0
# 环境：python 2.7
# 组件：
# 描述：
# 备注：
#-------------------------------------------------------

import sys
import logging
sys.path.append("../lib")
from ini_parse import *

def UnitTest():
    myIni = CIniParse()

    print 'load file'
    res = myIni.LoadIniFile('ini_test11.ini')
    print res

    print 'get all sec'
    res = myIni.GetAllSection()
    print res

    print 'get assign sec'
    res = myIni.GetAllItems('MEMSERVER')
    print res

    print 'get sec item'
    res = myIni.GetAttribValue('MEMSERVER','SERVERCNT')
    print res
    print type(res)

    print 'get host port'
    serlist = []
    j = int(res)
    for i in range(j):
        ser ={}
        ser['HOST%s' % (i)] = myIni.GetAttribValue('MEMSERVER', 'HOST%s' %(i))
        ser['PORT%s' % (i)] = int(myIni.GetAttribValue('MEMSERVER', 'PORT%s' %(i)))
        serlist.append(ser)
    print serlist

def main():
    args = sys.argv
    UnitTest()

if __name__ == '__main__':
    print 'sys.args = ' + __name__
    print sys.argv
    logging.warning('call mian FFF')
    main()